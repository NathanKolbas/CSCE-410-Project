import argparse
import math
import os

from directory_search import get_movie_list
from inverted_index import InvertedIndex
from lict_data import LictConfig

# Setup commandline args
parser = argparse.ArgumentParser(
    prog='TODO Change Later: Some kind of special index',
    description='Build an index for all files in a directory',
    epilog=' - A Team of Softies',
)

# The starting directory, defaults to CWD. Can specify a relative path to the CWD.
parser.add_argument('-d', '--dir', default=os.getcwd(), type=str)
# If the index should be built
parser.add_argument('-i', '--index')

# The commandline args
args = parser.parse_args()


def highlight_term(id, term, text):
    replaced_text = text.replace(term, "\033[1;32;40m {term} \033[0;0m".format(term=term))
    return "--- document {id}: {replaced}".format(id=id, replaced=replaced_text)


def load_documents():
    doc_ids = ['./test.txt']
    docs = []
    for doc in doc_ids:
        with open(doc, 'r', encoding="utf8", errors='ignore') as textfile:
            data = textfile.read().replace('\n', ' ').strip()
            docs.append({
                'id': doc,
                'text': data
            })
    print(docs[0])
    return docs


def load_document(f_path, id):
    with open(f_path, 'r', encoding="utf8", errors='ignore') as textfile:
        data = textfile.read().replace('\n', ' ').strip()
        return {
            'id': id,
            'text': data
        }


if __name__ == '__main__':
    print('------ STARTING ------')
    cwd = os.getcwd()
    is_absolute_path = os.path.isabs(args.dir)

    # The root path to start at
    root_path = args.dir if is_absolute_path else os.path.join(cwd, args.dir)
    print(f'Root DIR is: {root_path}')

    # Load the config
    config = LictConfig.open(root_path)
    print('Opened config...')

    # The relative path from the root
    movie_paths = get_movie_list(root_path)
    # The full path to the movies
    movie_paths_full = [os.path.join(root_path, p) for p in movie_paths]
    # Combine since we need the absolute path to open the file but relative for tree and index
    paths_tuple = zip(movie_paths_full, movie_paths)

    # print(movie_paths)
    # print(movie_paths_full)

    # Check for file changes relative to the previously built index (if there is one)
    print('Checking for changes...')
    paths_to_index = []
    for paths in paths_tuple:
        f_path = paths[0]
        file_id = paths[1]
        should_index = config.should_index(f_path, file_id)
        if should_index:
            paths_to_index.append(paths)

    # Build index for each file that has been changed
    print('Building index...')
    index = InvertedIndex()
    j = 0
    for i, paths in enumerate(paths_to_index):
        index.reset()
        j += 1
        f_path = paths[0]
        file_id = paths[1]
        print(f'\r{math.ceil(i / len(paths_to_index))}% - building index for: {file_id}', end='', flush=True)

        document = load_document(f_path, file_id)
        index.index_document(document)
        # print(index.index)
        index.save(f_path)

        config.indexed_file(f_path, file_id)
        # TODO: Temp just to stop before going too far...
        if j == 13:
            break
    print('\r100% - Index building complete!', end='', flush=True)

    # Save the config for later runs
    config.save(root_path)

    # print('Hello World!')
    # db = Database()
    # index = InvertedIndex(db, False)
    # documents = load_documents()
    # for document in documents:
    #     index.index_document(document)
    #
    # print(index.db)
    # print(index.index)
    #
    # while True:
    #     search_term = input("Enter term(s) to search: ")
    #     result = index.lookup_query(search_term)
    #
    #     for term in result.keys():
    #         for appearance in result[term]:
    #             # Belgium: { doc_id: 1, frequency: 1}
    #             document = db.get(appearance.doc_id)
    #             print(highlight_term(appearance.doc_id, term, document['text']))
    #         print("-----------------------------")
