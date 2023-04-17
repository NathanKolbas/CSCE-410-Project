import math
import os
from dataclasses import dataclass, field
from pathlib import Path
from queue import PriorityQueue
from typing import Any

from helpers import file_changes, load_document
from inverted_index import InvertedIndex
from lict_data import LictConfig


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


class Node:
    """
    A node in the tree
    """

    combined_indexes_dir_filename = 'combined_dir'
    combined_indexes_full_filename = 'combined_full'

    def __init__(self, node_id='', parent=None, children=None, items=None, level=0):
        # The id of the node which in one case might be a file path relative to root
        self.node_id: str = node_id
        # The parent Node that this Node belongs to. None if the root.
        self.parent: Node | None = parent
        # The child Nodes that are under this Node
        self.children: list[Node] = [] if children is None else children
        # All the items that are contained at this Node
        self.items: list[Any] = [] if items is None else items
        # The level from the root where root starts at 0
        self.level: int = level

    def __repr__(self):
        """
        String representation of the Node object
        """
        return str(self.__dict__)

    def is_leaf(self):
        return len(self.children) == 0

    def is_root(self):
        return self.parent is None

    def combine_indexes_dir(self, root_path: str):
        combined_index = InvertedIndex()
        for item in self.items:
            item_path = os.path.join(root_path, self.node_id, item)
            index = InvertedIndex.open(item_path)
            if index is not None:
                combined_index.combine(index)
        file_name = os.path.join(root_path, self.node_id, Node.combined_indexes_dir_filename)
        combined_index.save(file_name)

    def combine_indexes_full(self, root_path: str):
        item_path = os.path.join(root_path, self.node_id, Node.combined_indexes_dir_filename)
        combined_index = InvertedIndex.open(item_path)

        # Must run combine_indexes_dir first
        assert combined_index is not None

        if not self.is_leaf():
            for item in self.children:
                item_path = os.path.join(root_path, item.node_id, Node.combined_indexes_full_filename)
                index = InvertedIndex.open(item_path)
                if index is not None:
                    combined_index.combine(index)
        file_name = os.path.join(root_path, self.node_id, Node.combined_indexes_full_filename)
        combined_index.save(file_name)


class Item:
    """
    Represents an item located at a Node
    Currently not used...
    """

    def __init__(self, item_id='', node: Node = None, level=0):
        # The id of the Item which in one case might be a file path relative to root
        self.item_id: str = item_id
        # The Node that this item belongs to
        self.node: Node = node
        # The level from the root where root starts at 0
        self.level: int = level

    def __repr__(self):
        """
        String representation of the Item object
        """
        return str(self.__dict__)


class Tree:
    """
    A simple tree structor used to improve performance
    """

    def __init__(self, root_node=None, node_dict=None, level_dict=None):
        self.root_node: Node = root_node
        self.node_dict: dict = dict() if node_dict is None else node_dict
        self.level_dict: dict = dict() if level_dict is None else level_dict

        self.lowest_level = 0

    def __repr__(self):
        """
        String representation of the Tree object
        """
        return str(self.__dict__)

    @staticmethod
    def build_tree(root_path: str):
        tree = Tree()

        # First set up the root_node
        walk = os.walk(root_path)
        _, __, files = next(walk)
        files = [file for file in files if file.endswith(".txt")]
        root_node = Node(node_id='.', items=files)
        tree.node_dict['.'] = root_node
        tree.root_node = root_node

        for root, dirs, files in walk:
            path = Path(root)
            files = [file for file in files if file.endswith(".txt")]
            rel_path = path.relative_to(root_path)
            parent_id = str(rel_path.parent)
            parent_node = tree.node_dict[parent_id]

            node = Node(node_id=str(rel_path), items=files)
            tree.insert_node(parent_node, node)

        return tree

    @staticmethod
    def file_path_to_node_id(path: str):
        """
        Given the relative-from-root path to a file find the corresponding Node id
        """
        return str(Path(path).parent)

    def file_path_to_node(self, path: str):
        """
        Given the relative-from-root path to a file find the corresponding Node
        """
        node_id = self.file_path_to_node_id(path)
        return self.node_dict[node_id]

    def insert_node(self, parent_node: Node, new_node: Node):
        if parent_node is None:
            # Then this inserted Node is the root
            pass
        else:
            new_node.parent = parent_node
            new_node.level = parent_node.level + 1
            parent_node.children.append(new_node)

        self.node_dict[new_node.node_id] = new_node

        if new_node.level not in self.level_dict:
            self.level_dict[new_node.level] = []
        self.level_dict[new_node.level].append(new_node)

        self.lowest_level = max(self.lowest_level, new_node.level)

    def leaves(self):
        return [node for node in self.node_dict.values() if node.is_leaf()]

    def build_index(self, root_path: str, config: LictConfig):
        print('Checking for changes...')
        # Get all the files that have been changed/should be indexed
        changes, deleted = file_changes(root_path, config)

        # Remove deleted indexes for deleted files
        if len(deleted) != 0:
            print('Removing stale indexes...')
            for path in deleted:
                # Also remove from config
                key = os.path.relpath(path, start=root_path)
                if key in config.index_changes_dict:
                    del config.index_changes_dict[key]

                path = f'{path}{InvertedIndex.extension}'
                if os.path.exists(path):
                    os.remove(path)

        print('Building index...')
        # All these changes need to have their index rebuilt
        # Build index for each file that has been changed
        index = InvertedIndex()
        for i, paths in enumerate(changes):
            index.reset()
            f_path = paths[0]
            file_id = paths[1]
            print(f'\r{math.ceil(i / len(changes) * 100)}% - building index for: {file_id}', end='', flush=True)

            document = load_document(f_path, file_id)
            index.index_document(document)
            index.save(f_path)

            config.indexed_file(f_path, file_id)
        print('\r100% - Index building for files complete!', end='', flush=True)
        print('')

        # Save the config for later runs
        config.save(root_path)

        # Need to find any indexes that have been deleted

        print('Merging indexes...')
        # Need to then find all the Nodes that need to be combined
        # Each Node needs to have its parent recursively rebuilt too
        # First, find all the Node ids
        node_ids = set()
        for paths in changes + deleted:
            f_path = paths[0]
            file_id = paths[1]
            node = self.file_path_to_node(file_id)
            node_ids.add(node.node_id)
            while not node.is_root():
                node = node.parent
                node_ids.add(node.node_id)

        # Create a priority queue as we need to go from the furthest level down up
        pq = PriorityQueue()
        for node_id in node_ids:
            node = self.node_dict[node_id]
            # Invert priority (make it negative) since it goes from lowest number first
            pq.put(PrioritizedItem(priority=-node.level, item=node))

        # Combine nodes
        i = 0
        pq_length = pq.qsize()
        while not pq.empty():
            i += 1
            node = pq.get().item
            print(f'\r{math.ceil(i / pq_length * 100)}% - merging: {node.node_id}', end='', flush=True)
            node.combine_indexes_dir(root_path)
            node.combine_indexes_full(root_path)
        print('\r100% - Merging complete!', end='', flush=True)
        print('')

        # The index is built
        print('Index building complete!')
