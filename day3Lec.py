"""Convert words to vectores tha can be used with classifiers"""

# from sklearn.feature_extraction.text import CountVectorizer
# # list of text documents
# text = ["The quick brown fox jumped over the lazy dog."]
# # create the transform
# vectorizer = CountVectorizer()
# # tokenize and build vocab
# vectorizer.fit(text)
# # summarize
# print(vectorizer.get_feature_names())   #show a dictionary including all key words(output as a list)
# print(vectorizer.vocabulary_)   #output all keywords and their positions(according to the initial letter of alphabet) in a matrix
# # encode document
# vector = vectorizer.transform(text)
# # summarize encoded vector
# print(vector.shape)     #output a matrix (amount of strings, amount of key words)
# print(vector.toarray()) #output a matrix
#                         # each row represents a string
#                         # there are *n columns, *n is the amount of key words. Their positions represent the positions of key words
#                         # for each row, value of each position is number of corresponding position's key word(if none, output 0)
#
# #Try another sentence
# text2 = ["the quick puppy"]
# vector = vectorizer.transform(text2)
# print(vector.toarray())     #if none, output 0


"""BOW model is not very effeictive. represents presence or absence of a token in a document.
Lets keep count of tokens in a document

Using TFIDF instead of BOW, TFIDF also takes into account the frequency instead of just the occurance.
calculated as:
Term frequency = (Number of Occurrences of a word)/(Total words in the document) : normalizes based on the size of the document.
IDF(word) = Log((Total number of documents)/(Number of documents containing the word)) : reduces the impact  words that are common across documents, eg. the.
TF-IDF is the product of the two."""

from sklearn.feature_extraction.text import TfidfVectorizer
# list of text documents
text = ["The quick brown fox jumped over the lazy dog.",
		"The dog.",
		"The fox"]
# create the transform
vectorizer = TfidfVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
print(vectorizer.get_feature_names())
print(vectorizer.vocabulary_)
print(vectorizer.idf_)
# encode document
vector = vectorizer.transform([text[1]])
# summarize encoded vector
print(vector.shape)		# because it is defined as text[n], the former value is always 1 (only one string)
print(vector.toarray())








""" Extracting n grams from text """
# import  nltk
#
# all = []
# text = nltk.word_tokenize("The quick brown fox jumped on the dog")
# def find_bigrams(input_list):
#     bigram_list = []
#     for i in range(len(input_list)-1):
#         bigram_list.append((input_list[i], input_list[i+1]))
#     all.append(bigram_list)
#     # print(bigram_list)
#     return bigram_list
#
# #get individual items from the bigram
# bigrams = find_bigrams(text)
# print(all)
# print(bigrams)
# print(bigrams[0].__getitem__(0))
# print(bigrams[0].__getitem__(1))
#
# #Now write a function to generate trigrams.
# def find_trigrams(input_list):
# 	trigrams_list = []
# 	for i in range(len(input_list) - 2):
# 		trigrams_list.append(((input_list[i], input_list[i + 1], input_list[i + 2])))
# 	return trigrams_list
#
# trigrams = find_trigrams(text)
# print(trigrams)


"""using the nltk ngrams function"""
# from nltk import ngrams
# sentence = 'The quick brown fox jumped over the dog.'
# n = 6
# sixgrams = ngrams(sentence.split(), n)
# ngrams = []
# for grams in sixgrams:
#   ngrams.append(grams)
# print(ngrams)
