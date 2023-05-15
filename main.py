import argparse
import os
import shutil
import time
from pathlib import Path
from tabulate import tabulate

import inverted_index

from directory_search import get_index_files
from lict_data import LictConfig
from models.tree import Tree, Node
from old_approach import build_index, search_index

# Setup commandline args
parser = argparse.ArgumentParser(
    prog='TODO Change Later: Some kind of special index',
    description='Build an index for all files in a directory',
    epilog=' - A Team of Softies',
)

# The starting directory, defaults to CWD. Can specify a relative path to the CWD.
parser.add_argument('-d', '--dir', default=os.getcwd(), type=str)
# If the index should be built
parser.add_argument('-i', '--index', default=False, type=bool)
# The file type to build the index for
parser.add_argument('-e', '--extension', default='.txt', type=str)
# Removes all built index files
parser.add_argument('-c', '--clean', default=False, type=bool)
# Begin search
parser.add_argument('-s', '--search', default=True, type=bool)
# Begin comparison
parser.add_argument('-compare', '--compare', default=False, type=bool)

# The commandline args
args = parser.parse_args()


def highlight_term(doc_id, term, text):
    replaced_text = text.replace(term, "\033[1;32;40m {term} \033[0;0m".format(term=term))
    return "--- document {id}: {replaced}".format(id=doc_id, replaced=replaced_text)


def main():
    print('------ STARTING ------')
    cwd = os.getcwd()
    is_absolute_path = os.path.isabs(args.dir)

    if args.compare:
        root_path = args.dir if is_absolute_path else os.path.join(cwd, args.dir)
        if not os.path.exists(root_path) or not os.path.isdir(root_path):
            root_path = 'compare_corpus_original'
        else:
            root_path = os.path.relpath(root_path, cwd)

        print(f'Root DIR is: {root_path}')
        print('------ BEGINNING COMPARISON ------')
        compare_corpus_original = os.path.join(cwd, root_path)
        compare_corpus_old_approach = os.path.join(cwd, 'compare_corpus_old_approach')
        compare_corpus_new_approach = os.path.join(cwd, 'compare_corpus_new_approach')

        print('Cleaning the comparison directory')

        def remove_test_dirs():
            if os.path.exists(compare_corpus_old_approach):
                shutil.rmtree(compare_corpus_old_approach)
            if os.path.exists(compare_corpus_new_approach):
                shutil.rmtree(compare_corpus_new_approach)

        remove_test_dirs()
        shutil.copytree(compare_corpus_original, compare_corpus_old_approach)
        shutil.copytree(compare_corpus_original, compare_corpus_new_approach)

        def folder_size(f_path):
            root_directory = Path(f_path)
            return sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())

        compare_corpus_old_approach_init_size = folder_size(compare_corpus_old_approach)
        compare_corpus_new_approach_init_size = folder_size(compare_corpus_new_approach)

        # --------- BUILDING ---------
        print('Comparing initial build times...')

        print('Building index for old approach')

        def build_index_old():
            tic = time.perf_counter()  # Start Time
            old_index, old_db = build_index(compare_corpus_old_approach)
            toc = time.perf_counter()  # End Time
            return toc - tic, old_index, old_db

        index_build_time_old, old_index, old_db = build_index_old()

        print('Building index for new approach')

        def build_index_new():
            tic = time.perf_counter()  # Start Time
            config = LictConfig.open(compare_corpus_new_approach)
            tree = Tree.build_tree(compare_corpus_new_approach, '.txt')
            tree.build_index(compare_corpus_new_approach, config, '.txt')
            toc = time.perf_counter()  # End Time
            return toc - tic

        index_build_time_new = build_index_new()

        print('Rebuilding index for file deletion')

        def get_file(f_path):
            return os.path.join(f_path, 'small', 'test.txt')

        def delete_file(f_path):
            d_file = get_file(f_path)
            if os.path.exists(d_file):
                os.remove(d_file)

        print('Rebuilding index for old approach')
        delete_file(compare_corpus_old_approach)
        index_build_time_old_delete, old_index, old_db = build_index_old()

        print('Rebuilding index for new approach')
        delete_file(compare_corpus_new_approach)
        index_build_time_new_delete = build_index_new()

        print('Rebuilding index for file modification')

        def modify_file(f_path):
            d_file = get_file(f_path)
            with open(d_file, "wt") as f:
                f.write('This is some modification text')

        print('Rebuilding index for old approach')
        modify_file(compare_corpus_old_approach)
        index_build_time_old_modification, old_index, old_db = build_index_old()

        print('Rebuilding index for new approach')
        modify_file(compare_corpus_new_approach)
        index_build_time_new_modification = build_index_new()

        print('Rebuilding index for file creation')

        def create_file(f_path):
            d_file = os.path.join(f_path, 'NewFile.txt')
            with open(d_file, "wt") as f:
                f.write('This is some text for the new file')

        print('Rebuilding index for old approach')
        create_file(compare_corpus_old_approach)
        index_build_time_old_creation, old_index, old_db = build_index_old()

        print('Rebuilding index for new approach')
        create_file(compare_corpus_new_approach)
        index_build_time_new_creation = build_index_new()

        # --------- STORAGE ---------
        compare_corpus_old_approach_final_size = folder_size(compare_corpus_old_approach)
        compare_corpus_new_approach_final_size = folder_size(compare_corpus_new_approach)

        # --------- SEARCHING ---------
        search_term = 'nice'
        search_sub_dir = ''
        print('Searching for old approach')
        tic = time.perf_counter()  # Start Time

        found = search_index(old_index, old_db, search_term)

        toc = time.perf_counter()  # End Time
        index_search_time_old = toc - tic

        print('Searching for new approach')
        # Ignoring the loading of the index file for an equal comparison
        index_path = os.path.join(compare_corpus_new_approach, search_sub_dir, Node.combined_indexes_full_filename)
        index = inverted_index.InvertedIndex.open(index_path)

        tic = time.perf_counter()  # Start Time

        index.lookup_query(search_term)

        toc = time.perf_counter()  # End Time
        index_search_time_new = toc - tic

        search_sub_dir = 'small'
        print('Searching for old approach in sub dir')
        search_sub_dir_full = os.path.join(compare_corpus_old_approach, search_sub_dir)
        tic = time.perf_counter()  # Start Time

        found = [found for found in search_index(old_index, old_db, search_term) if found.find(search_sub_dir_full) != -1]

        toc = time.perf_counter()  # End Time
        index_search_time_old_subdir = toc - tic

        print('Searching for new approach in sub dir')
        # Ignoring the loading of the index file for an equal comparison
        index_path = os.path.join(compare_corpus_new_approach, search_sub_dir, Node.combined_indexes_full_filename)
        index = inverted_index.InvertedIndex.open(index_path)

        tic = time.perf_counter()  # Start Time

        index.lookup_query(search_term)

        toc = time.perf_counter()  # End Time
        index_search_time_new_subdir = toc - tic

        # Building index
        print('-------- Building index --------')
        print(f"Old index build finished in {index_build_time_old:0.4f} seconds")
        print(f"New index build finished in {index_build_time_new:0.4f} seconds")
        print(f"Old index rebuild after delete finished in {index_build_time_old_delete:0.4f} seconds")
        print(f"New index rebuild after delete finished in {index_build_time_new_delete:0.4f} seconds")
        print(f"Old index rebuild after modification finished in {index_build_time_old_modification:0.4f} seconds")
        print(f"New index rebuild after modification finished in {index_build_time_new_modification:0.4f} seconds")
        print(f"Old index rebuild after addition finished in {index_build_time_old_creation:0.4f} seconds")
        print(f"New index rebuild after addition finished in {index_build_time_new_creation:0.4f} seconds")

        # Index storage usage
        print('-------- Index storage usage --------')
        print(f"The amount of storage used initially for old approach was {compare_corpus_old_approach_init_size} bytes")
        print(f"The amount of storage used after building index for old approach was {compare_corpus_old_approach_final_size} bytes")
        print(f"The amount of storage increase used by old approach was {(compare_corpus_old_approach_final_size / compare_corpus_old_approach_init_size):0.4f}x")
        print(f"The amount of storage used initially for new approach was {compare_corpus_new_approach_init_size} bytes")
        print(f"The amount of storage used after building index for new approach was {compare_corpus_new_approach_final_size} bytes")
        print(f"The amount of storage increase used by new approach was {(compare_corpus_new_approach_final_size / compare_corpus_new_approach_init_size):0.4f}x")

        # Index searching
        print('-------- Index searching --------')
        print(f"Old search index finished in {index_search_time_old:0.4f} seconds")
        print(f"New search index finished in {index_search_time_new:0.4f} seconds")
        print(f"Old search index subdir finished in {index_search_time_old_subdir:0.4f} seconds")
        print(f"New search index subdir finished in {index_search_time_new_subdir:0.4f} seconds")

        # Print tables
        table = [
            ['Category', 'Traditional Index', 'Lic-T', 'Description'],
            [
                'Index Build',
                f'{index_build_time_old:0.4f} seconds',
                f'{index_build_time_new:0.4f} seconds',
                'The time it takes to build the initial index',
            ],
            [
                'Index Rebuild Delete',
                f'{index_build_time_old_delete:0.4f} seconds',
                f'{index_build_time_new_delete:0.4f} seconds',
                'The time it takes to rebuild the index after a file has been deleted',
            ],
            [
                'Index Rebuild Modification',
                f'{index_build_time_old_modification:0.4f} seconds',
                f'{index_build_time_new_modification:0.4f} seconds',
                'The time it takes to rebuild the index after a file has been modified',
            ],
            [
                'Index Rebuild New',
                f'{index_build_time_old_creation:0.4f} seconds',
                f'{index_build_time_new_creation:0.4f} seconds',
                'The time it takes to rebuild the index after a new file has been added',
            ],
            [
                'Storage Initially',
                f'{compare_corpus_old_approach_init_size:0.4f} bytes',
                f'{compare_corpus_new_approach_init_size:0.4f} bytes',
                'The amount of storage used initially by the directory being indexed (should be the same)',
            ],
            [
                'Storage After Build',
                f'{compare_corpus_old_approach_final_size:0.4f} bytes',
                f'{compare_corpus_new_approach_final_size:0.4f} bytes',
                'The amount of storage used by the directory being indexed after indexed',
            ],
            [
                'Storage Increase',
                f'{(compare_corpus_old_approach_final_size / compare_corpus_old_approach_init_size):0.4f}x',
                f'{(compare_corpus_new_approach_final_size / compare_corpus_new_approach_init_size):0.4f}x',
                'The multiple of the initial storage to the new storage usage',
            ],
            [
                'Full Search',
                f'{index_search_time_old:0.4f} seconds',
                f'{index_search_time_new:0.4f} seconds',
                'The amount of time it takes to search the whole index',
            ],
            [
                'Subdir Search',
                f'{index_search_time_old_subdir:0.4f} seconds',
                f'{index_search_time_new_subdir:0.4f} seconds',
                'The amount of time it takes to search only a certain sub folder',
            ],
        ]
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

        remove_test_dirs()
        return

    # The root path to start at
    root_path = args.dir if is_absolute_path else os.path.join(cwd, args.dir)
    if not os.path.exists(root_path) or not os.path.isdir(root_path):
        print(f'Directory not found or path is not a directory: {root_path}')
        return
    print(f'Root DIR is: {root_path}')

    if args.clean:
        print('Cleaning index files...')

        index_files = get_index_files(root_path)
        # The full path to the movies
        index_files_full = [os.path.join(root_path, p) for p in index_files]
        config_file = os.path.join(root_path, LictConfig.filename_full)

        # Remove the config file
        if os.path.exists(config_file):
            os.remove(config_file)

        # Delete index files
        for index_file in index_files_full:
            if os.path.exists(index_file):
                os.remove(index_file)

        print('Done cleaning!')
        return

    if args.index:
        # Load the config
        print('Opening config...')
        config = LictConfig.open(root_path)
        tree = Tree.build_tree(root_path, args.extension)
        tree.build_index(root_path, config, args.extension)
        return

    if args.search:
        print('Booting up search...')

        search_sub_dir = ''
        show_file_content = False

        # Load the index
        index_path = os.path.join(root_path, search_sub_dir, Node.combined_indexes_full_filename)
        index = inverted_index.InvertedIndex.open(index_path)
        if index is None:
            print('Index file not found...')
            return

        while True:
            print(f'Searching directory (to change use chdir=DIR): ./{search_sub_dir}')
            search_term = input("Enter term(s) to search: ")

            if '-exit' == search_term:
                print('Exiting...')
                break

            if 'chdir=' in search_term:
                search_term = search_term.replace('chdir=', '')
                new_search_sub_dir = search_term

                index_path = os.path.join(root_path, new_search_sub_dir, Node.combined_indexes_full_filename)
                new_index = inverted_index.InvertedIndex.open(index_path)
                if new_index is None:
                    print('Index file not found...')
                    continue
                index = new_index
                search_sub_dir = new_search_sub_dir
                print(f'Changed search directory to: ./{search_sub_dir}')
                continue

            if 'show-file-content=' in search_term:
                search_term = search_term.replace('show-file-content=', '')
                show_file_content = search_term.lower() == 'true'
                if show_file_content:
                    print('Enabled show file content')
                else:
                    print('Disabled show file content')
                continue

            result = index.lookup_query(search_term)
            for term in result.keys():
                for appearance in result[term]:
                    doc_id = appearance['doc_id']
                    if show_file_content:
                        file = os.path.join(root_path, appearance['doc_id'])
                        with open(file, 'r', encoding="utf8", errors='ignore') as textfile:
                            document = textfile.read()
                            print(highlight_term(doc_id, term, document))
                    else:
                        print(f'--- document {doc_id}')
                print("-----------------------------")


if __name__ == '__main__':
    main()
