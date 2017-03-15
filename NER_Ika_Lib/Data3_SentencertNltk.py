#
# Using NLTK Library to convert paragraphs into sentences
# Author: Rezka Aufar
#

from __future__ import print_function
import nltk.data

f = open("newdata/training/prep/allSentences.txt", "w")

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

fp = open("newdata/training/prep/allParagraphs.txt","r")

data = fp.read()

list = []
#print '\n-----\n'.join(tokenizer.tokenize(data))
list = tokenizer.tokenize(data)
for element in list:
	print(element,file=f)