import re
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


def combine_indices(index1, index2):
    new_index = InvertedIndex(preprocess=False)
    new_index.index = index1.index
    for key in index2.index.keys():
        if key in new_index.index:
            new_index.index[key].append(index2.index[key])
        else:
            new_index.index[key] = index2.index[key]
    return new_index


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
