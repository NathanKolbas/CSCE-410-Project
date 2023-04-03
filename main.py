from inverted_index import Database, InvertedIndex


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


if __name__ == '__main__':
    print('Hello World!')
    db = Database()
    index = InvertedIndex(db, False)
    documents = load_documents()
    for document in documents:
        index.index_document(document)

    print(index.db)
    print(index.index)

    while True:
        search_term = input("Enter term(s) to search: ")
        result = index.lookup_query(search_term)

        for term in result.keys():
            for appearance in result[term]:
                # Belgium: { doc_id: 1, frequency: 1}
                document = db.get(appearance.doc_id)
                print(highlight_term(appearance.doc_id, term, document['text']))
            print("-----------------------------")
