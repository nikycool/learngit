import re
import gensim
import os
import itertools
import numpy as np
import argparse
import string
from nltk.corpus import stopwords
import glob
from bs4 import BeautifulSoup
#from mycounter import Counter
import math
import pickle
from sklearn.metrics import pairwise
from nltk.stem import WordNetLemmatizer
from difflib import SequenceMatcher
import random
#对所有数据文本进行处理


wordnet_lemmatizer = WordNetLemmatizer()
engstop = stopwords.words('english')
set_stopword=engstop
parser = argparse.ArgumentParser("Word2Vec")


def lemmaorstem(w):
	return wordnet_lemmatizer.lemmatize(w)
	

	
def procline(q,stem=True):
	q=q.replace('Which of the following ','').replace('Which of these ','').replace('Which statement best describes ','')
	q=q.replace('Were do ','').replace('If a ','').replace('In which ','').replace('Which best ','').replace('What are ', '')
	q=q.replace('What best ','').replace('What is ','').replace('What would ', '').replace('When a ','').replace('Which statement ', '')
	q=q.replace('Why is ','').replace('Which ','')
	q = q.replace('\t',' ').replace('\n',' ').replace('\r', ' ').replace('  ',' ').replace('  ',' ').replace('  ',' ')
	q = re.sub('[^a-zA-Z0-9\- \']+', " ", q)
	if stem==False:
		q=[m  for m in q.lower().split(' ') if m not in set_stopword and m!='' and m!=' ']
	else:
		q=[lemmaorstem(m)  for m in q.lower().split(' ') if m not in set_stopword and m!='' and m!=' ']
	return q
	
	
def genlemmas():
	
	sents2=[]
	i = 0;
	for line in open('C:/Users/史淼/Desktop/Allen_AI_Kaggle-master/train/train/CK12clean.txt'):
		sent=procline(line)
		#print(sent)
		sents2.append(' '.join(sent))
		#print(sents2)
		
	f=open('C:/Users/史淼/Desktop/Allen_AI_Kaggle-master/train/trains/CK12lemma.txt','wb+')
	for se in sents2:
		#print(se)
		s=bytes(se+'\n', encoding="UTF-8")
		f.write(s)
	#f.write('\n'.join(sents3))
	f.close()
		
	lines={}
	lines2=[]
	for line in open('C:/Users/史淼/Desktop/Allen_AI_Kaggle-master/train/train/bigquiz.txt'):
		line=line.split('\t')
		line=' '.join(line[1:])
		lines[line]=None
		
	for line in lines:
		sent=procline(line)
		lines2.append(' '.join(sent))
	f=open('C:/Users/史淼/Desktop/Allen_AI_Kaggle-master/train/trains/bigquizlemma.txt','wb+')
	for se in lines2:
		#print(se)
		s=bytes(se+'\n', encoding="UTF-8")
		f.write(s)
	#f.write('\n'.join(lines2))
	f.close()
		

	lines={}
	lines2=[]
	for line in open('C:/Users/史淼/Desktop/Allen_AI_Kaggle-master/train/train/bigquiz2.txt'):
		line=line.split('\t')
		line=' '.join(line[1:])
		lines[line]=None
		
	for line in lines:
		sent=procline(line)
		lines2.append(' '.join(sent))
		#sents.append(sent)
	f=open('C:/Users/史淼/Desktop/Allen_AI_Kaggle-master/train/trains/bigquizlemma2.txt','wb+')
	for se in lines2:
		#print(se)
		s=bytes(se+'\n', encoding="UTF-8")
		f.write(s)
	#f.write('\n'.join(lines2))
	f.close()
	
	lines={}
	lines2=[]
	for line in open('C:/Users/史淼/Desktop/Allen_AI_Kaggle-master/train/train/bigquiz3.txt'):
		line=line.split('\t')
		line=' '.join(line[1:])
		lines[line]=None
		
	for line in lines:
		sent=procline(line)
		lines2.append(' '.join(sent))
		#sents.append(sent)
	f=open('C:/Users/史淼/Desktop/Allen_AI_Kaggle-master/train/trains/bigquizlemma3.txt','wb+')
	for se in lines2:
		#print(se)
		s=bytes(se+'\n', encoding="UTF-8")
		f.write(s)
	#f.write('\n'.join(lines2))
	f.close()
		
	
genlemmas()