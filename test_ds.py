from reccomendations.user_event import UserPerfectEvent

def main():
	json_data = [{
			"id": 132,
            "title": "Концерт в парке",
            "text": "Интересный концерт в парке",
            "spheres": ['Спектакли', 'Чтения'],
	},
	{
			"id": 124,
            "title": "Концерт в парке",
            "text": "Интересный концерт в парке",
            "spheres": ['Спектакли', 'Концерты'],
	}]

	user = UserPerfectEvent(json_data)

	a = ['для одного', 'для двоих', 'компания друзей']
	print(a)
	user.set_answer(a)

	json_question = user.get_questions()

	print(json_question['question'])
	for i in json_question['possible_answers']:
		print(i)
	user.set_answer(json_question['possible_answers'][0])

	user.set_answer('skip')

	reccomendations = user.get_events()

	print(reccomendations['reccomendations'])

if __name__ == '__main__':
    main()

