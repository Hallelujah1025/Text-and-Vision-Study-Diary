from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import nltk


def searchPronouns(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    pronouns = []
    for i in chunked:
        if type(i) == tuple:
            if i[1] == 'PRP' or i[1] == 'PRP$':
                pronouns.append(i)
    print(pronouns)

    named_entity = []
    for pronoun in pronouns:
        if pronoun[0].lower() != 'it' and pronoun[0].lower() != 'its' and pronoun[0].lower() != 'they' and pronoun[0].lower() != 'them':
            print("PERSON: ", pronoun[0])


file = open("D:/STUDY/Text and Vision Intelligence/CJLU day 4/trucks articls.txt")
txt = file.read()
searchPronouns(txt)
