import re
import os

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


class Appearance:
    """
    Represents the appearance of a term in a given document, along with the
    frequency of appearances in the same one.
    """

    def __init__(self, doc_id, frequency):
        self.doc_id = doc_id
        self.frequency = frequency

    def __repr__(self):
        """
        String representation of the Appearance object
        """
        return str(self.__dict__)



def from_doc_to_terms(doc):
    """
    Takes a doc (giant string) and gets the terms
    """
    tokens = nltk.word_tokenize(doc.strip())
    tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stopwords.words('english')]
    return tokens


class InvertedIndex:
    """
    Inverted Index class.
    """

    def __init__(self, preprocess=False):
        self.index = dict()
        self.preprocess = preprocess

    def __repr__(self):
        """
        String representation of the Database object
        """
        return str(self.index)

    def index_document(self, document):
        """
        Process a given document, save it to the DB and update the index.
        """
        if self.preprocess:
            terms = from_doc_to_terms(document['text'])
            appearances_dict = dict()
            for term in terms:
                appearances_dict[term] = Appearance(document['id'], 0)
        else:
            # Remove punctuation from the text.
            clean_text = re.sub(r'[^\w\s]', '', document['text'])
            terms = clean_text.split(' ')
            appearances_dict = dict()
            # Dictionary with each term and the frequency it appears in the text.
            for term in terms:
                term_frequency = appearances_dict[term].frequency if term in appearances_dict else 0
                appearances_dict[term] = Appearance(document['id'], term_frequency + 1)

        # Update the inverted index
        update_dict = {key: [appearance]
        if key not in self.index
        else self.index[key] + [appearance]
                       for (key, appearance) in appearances_dict.items()}
        self.index.update(update_dict)
        # Add the document into the database
        self.db.add(document)
        return document

    def lookup_query(self, query):
        """
        Returns the dictionary of terms with their correspondent Appearances.
        This is a very naive search since it will just split the terms and show
        the documents where they appear.
        """
        if self.preprocess:
            return {term: self.index[term] for term in from_doc_to_terms(query) if term in self.index}
        else:
            return {term: self.index[term] for term in query.split(' ') if term in self.index}
    

def combine_indices(index1, index2):
    new_index = InvertedIndex(preprocess=False)
    new_index.index = index1.index
    for key in index2.index.keys():
        if key in new_index.index:
            new_index.index.append(index2.index[key])
        else:
            new_index.index[key] = index2.index[key]
    return new_index


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
    index = InvertedIndex(preprocess=False)
    documents = load_documents()
    for document in documents:
        index.index_document(document)

    print(index.db)
    print(index.index)

    while True:
        search_term = input("Enter term(s) to search: ")
        result = index.lookup_query(search_term)

        # TODO: Print out text from found documents
        #for term in result.keys():
        #    for appearance in result[term]:
        #        # Belgium: { doc_id: 1, frequency: 1}
        #        document = db.get(appearance.doc_id)
        #        print(highlight_term(appearance.doc_id, term, document['text']))
        #    print("-----------------------------")
