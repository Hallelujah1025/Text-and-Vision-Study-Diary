# from nltk.corpus import brown
# from nltk.book import *
# from nltk import sent_tokenize, word_tokenize, pos_tag
#
# print(brown.words()[0:10])
# print(len(brown.words()))
# print()
#
# print(texts())
# print(len(text1))
# print()
#
# text = "Text and Vision Intelligence is a course that deal with interpreting texts and images computationally. This has become increasingly important in " \
#        "the last decade due to a large amount of texts and images online as well offline."
# print(sent_tokenize(text))
# print(word_tokenize(text))
# print(pos_tag(word_tokenize(text)))







from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import nltk
import os

fileDir="D:/STUDY/Text and Vision Intelligence/Assignment1/example"
for root, dirs, files in os.walk(fileDir):
    articles = []
    for file in files:
        name,suffix = os.path.splitext(file)
        lines = []
        f = open(os.path.join(root,file),"r",encoding = 'utf-8')
        for line in f:
            lines.append(line.strip('\n'))
        tmp = ' '.join(lines)
        articles.append(tmp)
    str = ' '.join(articles)
print(str)
    # print(articles)

