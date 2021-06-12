from dataclasses import dataclass

@dataclass
class Qestions:
	main_questions = {
	1: 'Выберите район откуда Вы поедете на мероприятие',
	2: 'Когда планируете пойти на мероприятие',
	3: "В какое время планируете посещение?"
}
	сat_ask = 'Для кого ищете мероприятие?'
	categories_questions = {
		'для одного': ['Readings', 'Parks', 'Concerts', 'Education', 'Exhibition', 'Meetings', 'Fest', 'Sport', 'Theatres'],
		"для двоих": ['GuidedTours', 'Readings', 'Parks',  'Education', 'Concerts', 'Quests', 'Exhibition', 'Meetings', 'Fest', 'Sport', 'Theatres'],
		"компания друзей": ['GuidedTours', 'Readings', 'Parks', 'Concerts', 'Quests', 'Exhibition', 'Meetings', 'Fest', 'Sport'],
		"для детей": ['Readings', 'Parks', 'Childs', 'Quests', 'Exhibition', 'Fest', 'Sport'],
		"для всей семьи": ['GuidedTours', 'Readings', 'Parks', 'Education', 'Childs', 'Quests', 'Exhibition', 'Fest', 'Sport']
	}

	sphere_ask = 'Выберите, что Вам больше подходит?'
	sphere_questions = {
		'Readings': ['Почитать в компании стихи Цветаевой',],
		'Meetings': ['Провести время в компании единомышленников за интересным обсуждением'],
		'Fest': ["Посетить фестиваль"],
		'Sport': ['Заняться активным отдыхом'],
		'Theatres': ['Послушать Пиковую Даму',
			'Познакомиться с творчеством А.Райкина'],
		'Exhibition': ['Сходить на Мунка',
			'Посмотреть фото старой Москвы'],
		'Childs': ['Сходить с детьми на интересное мероприятие'],
		'Quests': ['Поучаствовать в квесте'],
		'Concerts': ['Послушать органную музыку'],
		'Education': ['Узнать что-то новое'],
		'Parks': ['Провести время на открытом воздухе'],
		'GuidedTours': ['Пройтись по историческим местам Басманного района',
			'Провести время на открытом воздухе'],
		}