import argparse
import os

from directory_search import get_movie_list
from inverted_index import Database, InvertedIndex


# Setup commandline args
parser = argparse.ArgumentParser(
    prog='TODO Change Later: Some kind of special index',
    description='Build an index for all files in a directory',
    epilog=' - A Team of Softies',
)

# The starting directory, defaults to CWD. Can specify a relative path to the CWD.
parser.add_argument('-d', '--dir', default=os.getcwd(), type=str)
# If the index should be built
parser.add_argument('-c', '--compile')

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


def load_document(f_path):
    with open(f_path, 'r', encoding="utf8", errors='ignore') as textfile:
        data = textfile.read().replace('\n', ' ').strip()
        return {
            'id': f_path,
            'text': data
        }


if __name__ == '__main__':
    print('------ STARTING ------')
    is_absolute_path = os.path.isabs(args.dir)

    # The root path to start at
    root_path = args.dir if is_absolute_path else os.path.join(os.getcwd(), args.dir)

    # The relative path from the root
    movie_paths = get_movie_list(root_path)
    # The full path to the movies
    movie_paths_full = [os.path.join(root_path, p) for p in movie_paths]

    print(movie_paths)
    print(movie_paths_full)

    for path in movie_paths:
        db = Database()
        index = InvertedIndex(db, False)
        document = load_document(path)
        index.index_document(document)
        print(index.db)
        print(index.index)


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
