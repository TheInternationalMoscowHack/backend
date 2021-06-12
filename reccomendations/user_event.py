from vectorizer import Vectorizer

class UserPerfectEvent:
	def __init__(self):
		self.vectorizer = Vectorizer()
		self.vectorizer.load_vectorizer()
		self.question_counter = 0

	def send_questions(self, answer=None, max_questions=6,
		n_reccomedations=16):
		"""
		Send user questions for user.
		If get answer - changes perfect vector and
		choose new answer
		"""
		pass

