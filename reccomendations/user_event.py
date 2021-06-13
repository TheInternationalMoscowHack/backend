from reccomendations.config import config
from reccomendations.questions import questions
from reccomendations.vectorizer import Vectorizer
from reccomendations.clean_text import clean_text

import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity as coss


class UserPerfectEvent:
	def __init__(self, data):
		self.vectorizer = Vectorizer()
		self.vectorizer.load_vectorizer(path=config.MODEL_VECTORIZER)
		self.question_counter = 0
		self.answers_ngrams = []
		self.data = pd.DataFrame(data)
		self.skip_flag = 'skip'
		self.max_questions = 3
		self.data['simil'] = 0
		self.count_ngrams = 3

		self.data['description'] = self.data['description'].map(clean_text)
		self.vectors = self.vectorizer.transform(self.data['description'])
		
		self.data['spheres'] = self.data['spheres'].map(
			lambda x: ";".join([i for i in x['sphere_name'].split(", ")]))


		self.spheres = set()
		for i in self.data['spheres'].unique():
			for j in i.split(';'):
				self.spheres.add(j)

		with open(config.SPHERES_WORDS, 'r') as fp:
			self.spheres_words = json.load(fp)



	def calc_top_themes(self, q, n):
		less = np.quantile(self.data['simil'], [(q - 1) * 0.25])[0]
		great = np.quantile(self.data['simil'] , [q * 0.25])[0]

		v = self.data[(great >= self.data['simil']) & (self.data['simil'] >= less)]['spheres'].value_counts().to_dict()
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
		res = self.data[self.data.simil > 0][['id', 'simil']].set_index('id')
		if len(res) == 0:
			return self.data.id.iloc[:n].tolist()
		res = {k: v for k, v in sorted(res.to_dict()['simil'].items(),
			key=lambda item: item[1], reverse=True)}
		if len(res) < n:
			return list(res.keys()) + self.data.id.iloc[:n - len(res)].tolist()
		return list(res.keys())[:n]


	def set_answer(self, answer):
		if answer == self.skip_flag:
			for theme in self.last_themes:
				ngramm = np.random.choice(list(self.spheres_words[theme].keys()))
				self.answers_ngrams.append(ngramm)

		elif isinstance(answer, list):
			for answ in answer:
				for theme in questions.categories_questions[answ]:
					ngramm = np.random.choice(list(self.spheres_words[theme].keys()))
					self.answers_ngrams.append(ngramm)
		else:
			answer_n = self.last_questions['possible_answers'].index(answer)
			ngrams = np.random.choice(list(self.spheres_words[self.last_themes[answer_n]].keys()),
				self.count_ngrams)
			self.answers_ngrams.extend(ngrams)
		X = self.vectorizer.transform([" ".join(self.answers_ngrams)]) 
		self.data['simil'] = coss(X, self.vectors)[0]


	def get_events(self, n_reccomedations=16):
		return {'reccomendations': self.get_top_events(n_reccomedations)}


	def get_questions(self):
		"""
		Send user questions for user.
		If get answer - changes perfect vector and
		choose new answer
		"""

		if self.question_counter >= self.max_questions:
			return self.get_events()

		themes = self.choose_themes()
		question = questions.sphere_ask
		possible_answers = []
		for i in themes:
			possible_answers.append(
				np.random.choice(questions.sphere_questions[i])) 
		
		self.last_themes = themes
		self.last_questions = {'question': question,
			"possible_answers": possible_answers} # ToDo: Проверка на то, что вопросы не повторятся
		self.question_counter += 1
		return self.last_questions
