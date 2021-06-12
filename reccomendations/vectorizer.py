import pickle

class Vectorizer:
	def train_vectorizer(self):
		pass

	def load_vectorizer(self, path):
		with open(path, 'rb') as f:
			self.vectorizer = pickle.load(f)

