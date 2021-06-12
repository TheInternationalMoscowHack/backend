import re
import pymorphy2

from nltk.corpus import stopwords

MORPH = pymorphy2.MorphAnalyzer()
STOP_WORDS = set(stopwords.words(["russian", "english"])) #  множество русско английских стоп слов
for i in ['nbsp', 'laquo', 'raquo', 'ndash', 'mdash', 'hellip', 'rdquo']:
    STOP_WORDS.add(i)

def clean_html(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  cleanr = re.compile(' &.*? ')
  cleantext = re.sub(cleanr, ' ', cleantext)
  return cleantext

def normalize_text_with_morph(text, morph):
    alphabet = 'abcdefghijklmnopqrstuvwxyzабвгдежзийклмнопрстуфхцчшщъыьэюя '

    text = text.lower().replace("ё", "е")
    words = ''.join([[" ", i][i in alphabet] for i in text]).lower().split()
    return ' '.join([morph.parse(w)[0].normal_form for w in words])

def clean_stopwords(text):
    return " ".join([word for word in text.split() if (word not in STOP_WORDS) and (len(word) > 1)])

def clean_text(text):
	text = clean_html(text)
	text = normalize_text_with_morph(text, MORPH)
	return clean_text(text)