from reccomendations.user_event import UserPerfectEvent

def main():
	json_data = {
			"id": 123,
            "title": "Концерт в парке",
            "description": "Интересный концерт в парке",
            "image": "http://events-hack.herokuapp.com/media/event_images/2021-06-13_12-11-12.png",
            "spot_name": "ЦПКиО",
            "address": "ул. Пушкина",
            "is_free": False,
            "date_from": "2021-06-01T18:00:00Z",
            "date_to": "2021-06-30T18:00:00Z",
            "restriction": 6,
            "district_name": "Центральный",
            "spheres": [
                {
                    "id": 1,
                    "sphere_name": "Спектакли",
                    "created_at": "2021-06-13T11:08:56.859725Z",
                    "modified_at": "2021-06-13T11:08:56.859725Z"
                }
            ],
            "themes": [
                {
                    "id": 1,
                    "theme_name": "События в парках",
                    "created_at": "2021-06-13T11:10:30.234704Z",
                    "modified_at": "2021-06-13T11:10:30.235739Z"
                }
            ]
	}

	user = UserPerfectEvent(json_data)

	json_question = user.get_questions()

	user.set_answer(list(json_question.values())[0][0])

	reccomendations = user.get_events()

	print(reccomendations['reccomendations'])

if __name__ == '__main__':
    main()
