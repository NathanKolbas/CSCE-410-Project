import re
import os

import nltk
from nltk.corpus import stopwords

from directory_search import get_files_list


class Appearance:
	"""
	Represents the appearance of a term in a given document, along with the
	frequency of appearances in the same one.
	"""

	def __init__(self, docId, frequency):
		self.docId = docId
		self.frequency = frequency

	def __repr__(self):
		"""
		String representation of the Appearance object
		"""
		return str(self.__dict__)


class Database:
	"""
	In memory database representing the already indexed documents.
	"""

	def __init__(self):
		self.db = dict()

	def __repr__(self):
		"""
		String representation of the Database object
		"""
		return str(self.__dict__)

	def get(self, id):
		return self.db.get(id, None)

	def add(self, document):
		"""
		Adds a document to the DB.
		"""
		return self.db.update({document['id']: document})

	def remove(self, document):
		"""
		Removes document from DB.
		"""
		return self.db.pop(document['id'], None)


def from_doc_to_terms(doc):
	tokens = nltk.word_tokenize(doc.strip())
	tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stopwords.words('english')]
	return tokens


class InvertedIndex:
	"""
	Inverted Index class.
	"""

	def __init__(self, db, preprocess=False):
		self.index = dict()
		self.db = db
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


def highlight_term(id, term, text):
	replaced_text = text.replace(term, "\033[1;32;40m {term} \033[0;0m".format(term=term))
	return "--- document {id}: {replaced}".format(id=id, replaced=replaced_text)


def load_documents(f_path):
	doc_ids = [os.path.join(f_path, file) for file in get_files_list(f_path, '.txt')]
	# print(docIds)

	documents = []
	for doc in doc_ids:
		with open(doc, 'r', encoding="utf8", errors='ignore') as textfile:
			data = textfile.read().replace('\n', ' ').strip()
			documents.append({
				'id': doc,
				'text': data
			})
	# print(documents[0])
	return documents


def build_index(f_path):
	db = Database()
	index = InvertedIndex(db)
	documents = load_documents(f_path)
	for document in documents:
		index.index_document(document)

	return index, db


def search_index(index, db, search_term):
	result = index.lookup_query(search_term)

	terms = []
	for term in result.keys():
		for appearance in result[term]:
			document = db.get(appearance.docId)
			terms.append(highlight_term(appearance.docId, term, document['text']))
	return terms


def main(f_path):
	db = Database()
	index = InvertedIndex(db)
	documents = load_documents(f_path)
	for document in documents:
		index.index_document(document)

	search_term = input("Enter term(s) to search: ")
	result = index.lookup_query(search_term)

	for term in result.keys():
		for appearance in result[term]:
			# Belgium: { docId: 1, frequency: 1}
			document = db.get(appearance.docId)
			print(highlight_term(appearance.docId, term, document['text']))
		print("-----------------------------")
