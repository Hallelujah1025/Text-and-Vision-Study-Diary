from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import nltk
import os

def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []
    #print(chunked)
    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    if continuous_chunk:
        named_entity = " ".join(current_chunk)
        if named_entity not in continuous_chunk:
            continuous_chunk.append(named_entity)

    return continuous_chunk


# a function to read all articles below a dir and convert them to one single str
def readArticles():
    # path of the specific dir I put in my own computer
    ref = "D:/STUDY/Text and Vision Intelligence/Assignment1/articles"
    dirs = os.listdir(ref)
    articles = []
    # traverse all files below the dir
    for file in dirs:
        with open(os.path.join(ref, file)) as f:
            lines = []
            # read each line and put them in the list lines[]
            for line in f.readlines():
                # drop unnecessary char
                line = line.strip('\n')
                line = line.strip('\'')
                lines.append(line)
            # transfer the list in one article to a str
            strArticle = ' '.join(lines)
        articles.append(strArticle)
    # transfer the list included all content to one single str
    strArticles = ' '.join(articles)
    return strArticles


txt = readArticles()
print(get_continuous_chunks(txt))


count = {}
for sent in nltk.sent_tokenize(txt):    # divide txt in sentences and traverse each sent
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
        if hasattr(chunk, 'label'):

            if chunk.label() in count:
                count[chunk.label()] += 1
            else:
                count[chunk.label()] = 1
print(count)

