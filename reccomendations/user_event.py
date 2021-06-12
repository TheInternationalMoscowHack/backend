from reccomendations.config import config
from reccomendations.questions import questions

from reccomendations.vectorizer import Vectorizer

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as coss


class UserPerfectEvent:
	def __init__(self, data):
		self.vectorizer = Vectorizer()
		self.vectorizer.load_vectorizer(path=config.MODEL_VECTORIZER)
		self.question_counter = 0
		self.answers = []
		self.data = data
		self.vectors = self.vectorizer.transform(data)
		self.data['sphere'] = self..spheres.map(
			lambda x: ";".join([i['title'] for i in x]))

		self.spheres = set()
		for i in self.data['sphere'].unique():
		    for j in i.split(';'):
		        self.spheres.add(j)



	def calc_top_themes(self, q, n):
		less = np.quantile(coss(X, tfidfs)[0], [(q - 1) * 0.25])[0]
		great = np.quantile(coss(X, tfidfs)[0], [q * 0.25])[0]

		v = self.data[(great >= self.data['dist']) & (self.data['dist'] >= less)]['type'].value_counts().to_dict()
  		keys = list(v.keys())
    	for i in keys:
        	if len(i.split(", ")) > 1:
            	for j in i.split(", "):
                	if j in v.keys():
                    	v[j] += v[i]
                	else:
                    	v[j] = v[i]
	            del v[i]
    	return sorted(v.items(), key=lambda item: item[1], reverse=True)[:n]


	def choose_themes(self):
		themes_1 = self.calc_top_themes(q=1, n=2)
		themes_2 = self.calc_top_themes(q=4, n=4)
		themes = [i for i, _ in themes_1]
		for i, _ in themes_2:
			if i not in themes:
				themes.append(i)
		return themes[:4]

	def get_top_events(self, n):
		res = self.data[data.dist > 0][['id', 'dist']].set_index('id')
		if len(res) == 0:
			return self.data.id.iloc[:n].tolist()
		res = {k: v for k, v in sorted(res.to_dict()['dist'].items(),
			key=lambda item: item[1], reverse=True)}
		if len(res) < n:
			return list(res.keys()) + self.data.id.iloc[:n - len(res)].tolist()
		return list(res.keys())[:n]


	def get_questions(self, answer=None, max_questions=3,
		n_reccomedations=16):
		"""
		Send user questions for user.
		If get answer - changes perfect vector and
		choose new answer
		"""
		if self.question_counter == 0:
			pass # выбор из 4 частотных тем

		if answer in questions.categories_questions:
			pass # ToDo: добавить слова из каждой категории
		else:
			self.answers.append(answer) # ToDo: заменить answer на набор топ слов из темы
		X = self.vectorizer.transform([" ".join(self.answers)]) 
		self.data['dist'] = coss(X, tfidfs)[0]

		if self.question_counter == max_questions:
			return {'reccomendations': self.get_top_events(n)}

		themes = self.choose_themes()
		question = questions.sphere_ask
		possible_answers = []
		for i in themes:
			possible_answers.append(
				np.random.choice(questions.sphere_questions[i])) 
		return {question: possible_answers}