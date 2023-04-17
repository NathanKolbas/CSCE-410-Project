import argparse
import os
import inverted_index

from directory_search import get_index_files
from lict_data import LictConfig
from models.tree import Tree, Node

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

# The commandline args
args = parser.parse_args()


def highlight_term(doc_id, term, text):
    replaced_text = text.replace(term, "\033[1;32;40m {term} \033[0;0m".format(term=term))
    return "--- document {id}: {replaced}".format(id=doc_id, replaced=replaced_text)


def main():
    print('------ STARTING ------')
    cwd = os.getcwd()
    is_absolute_path = os.path.isabs(args.dir)

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
        while True:
            print(f'Searching directory (to change use chdir=DIR): ./{search_sub_dir}')
            search_term = input("Enter term(s) to search: ")

            if 'exit' == search_term:
                print('Exiting...')
                break

            if 'chdir=' in search_term:
                search_term = search_term.replace('chdir=', '')
                search_sub_dir = search_term
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

            index_path = os.path.join(root_path, search_sub_dir, Node.combined_indexes_full_filename)
            index = inverted_index.InvertedIndex.open(index_path)
            if index is None:
                print('Index file not found...')
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
