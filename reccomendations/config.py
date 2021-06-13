from dataclasses import dataclass

@dataclass
class Configuration:
	DATA_PATH: str = './reccomendations/models/'
	MODEL_VECTORIZER: str = '{}tfidfv.pickle'.format(DATA_PATH)
	SPHERES_WORDS: str = '{}spheres_words.json'.format(DATA_PATH)
	STOP_WORDS: str = '{}stopwords.txt'.format(DATA_PATH)

config = Configuration()