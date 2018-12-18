import collections
import gensim
import word2phrase
#from gensim.models.word2vec import word2phrase
#from textblob import TextBlob
import pickle
#用word2phrase记录两个词和三个词的词频，保存在quizletvocab3.pick
def get_book():
	salida={}
	'''for line in open('./train/trains/bigquizlemma.txt'):
		salida[line]=None
	for line in open('./train/trains/bigquizlemma2.txt'):
		salida[line]=None
	for line in open('./train/trains/bigquizlemma3.txt'):
		salida[line]=None
	for line in open('./train/trains/CK12lemma.txt'):
		salida[line]=None
		'''
	for line in open('./train/trains/CK12.txt'):
		salida[line] = None
	return [m.split(' ') for m in salida.keys()]


def main():
	book_sentences = get_book()
	print(book_sentences)
	phrased1 = word2phrase.train_model(book_sentences, min_count=3)
	#phrased1 = bytes(phrased1, encoding="UTF-8")
	print(phrased1)
	phrased2 = word2phrase.train_model(phrased1, min_count=3)
	print(phrased2)
	#phrased2 = gensim.models.word2vec.word2phrase.train_model(phrased1, min_count=3)
	two_word_counter = collections.Counter()
	three_word_counter = collections.Counter()
	for sentence in phrased2:
		for word in sentence:
			if word.count('_') == 1:
				two_word_counter[word] += 1
			if word.count('_') == 2:
				three_word_counter[word] += 1
	print(two_word_counter)
	pickle.dump([two_word_counter,three_word_counter],open('./train/trains/quizletvocab3.pick','wb+'))
	print('=' * 60)
	print('Top 20 Two Word Phrases')
	for phrase, count in two_word_counter.most_common(20):
		print('%56s %6d' % (phrase, count))

	print
	print('=' * 60)
	print('Top 10 Three Word Phrases')
	for phrase, count in three_word_counter.most_common(10):
		print('%56s %6d' % (phrase, count))


if __name__ == '__main__':
	main()