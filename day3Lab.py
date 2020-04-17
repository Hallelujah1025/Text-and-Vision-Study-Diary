import nltk
import os

def readArticles(ref, article = []):
    dirs = os.listdir(ref)
    for file in dirs:
        with open(os.path.join(ref, file)) as f:
            article.append(f.read())

all = []
def analyseArticle(article = []):
    for i in range(len(article)):
        text = nltk.word_tokenize(article[i])
        def find_bigrams(input_list):
            bigram_list = []
            for i in range(len(input_list) - 1):
                bigram_list.append((input_list[i], input_list[i + 1]))

            return bigram_list

        # get individual items from the bigram
        bigrams = find_bigrams(text)
        # print(bigrams)
        all.append(bigrams)
        # return bigrams
    return all

singleBigram = []
def transform():
    for i in range(len(all)):
        for j in range(len(all[i])):
            singleBigram.append(all[i][j])


def countBigrams():
    count = {}
    for value in singleBigram:
        if value in count:
            count[value] += 1
        else:
            count[value] = 1

    print(count)
    maxValue = max(zip(count.values(), count.keys()))
    print(maxValue)
    # print(type(maxValue))

    for i in range(len(singleBigram)):
        if maxValue[1] == singleBigram[i]:
            if i - 1 < 0 or i + 1 >= len(singleBigram):
                print("out of index")
            else:
                print(singleBigram[i - 1], singleBigram[i + 1])



if __name__ == '__main__':
    article = []
    readArticles("D:/STUDY/Text and Vision Intelligence/CJLU day 3/terrorism data", article)
    # readArticles("D:/STUDY/Text and Vision Intelligence/CJLU day 3/example", article)

    # print(article)
    allBigrams = []
    analyseArticle(article)
    # print(all)

    transform()
    # print(singleBigram)

    countBigrams()



