from dataclasses import dataclass

@dataclass
class Configuration:
	DATA_PATH: str = './data/'
	MODEL_VECTORIZER: str = '{}tfidfvectorizer.model'.format(DATA_PATH)