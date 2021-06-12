from dataclasses import dataclass

@dataclass
class Configuration:
	DATA_PATH: str = './reccomendations/models/'
	MODEL_VECTORIZER: str = '{}tfidfv.pickle'.format(DATA_PATH)

config = Configuration()