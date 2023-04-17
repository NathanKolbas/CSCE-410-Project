import argparse
import os

from directory_search import get_index_files
from lict_data import LictConfig
from models.tree import Tree

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
# Removes all built index files
parser.add_argument('-c', '--clean', default=False, type=bool)

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


def main():
    print('------ STARTING ------')
    cwd = os.getcwd()
    is_absolute_path = os.path.isabs(args.dir)

    # The root path to start at
    root_path = args.dir if is_absolute_path else os.path.join(cwd, args.dir)
    print(f'Root DIR is: {root_path}')

    if args.clean:
        print('Cleaning index files...')

        index_files = get_index_files(root_path)
        # The full path to the movies
        index_files_full = [os.path.join(root_path, p) for p in index_files]
        config_file = os.path.join(root_path, LictConfig.filename)

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
        tree = Tree.build_tree(root_path)
        tree.build_index(root_path, config)
        return

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


if __name__ == '__main__':
    main()
