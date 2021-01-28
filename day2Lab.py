import nltk

# -------------------------------------------------------------------------------------------------------This is a demo to output specific nouns
passage = """His interest piqued, even though in his 60s (an age where many seniors are a little intimidated by new technology), 
              he persevered with it – mainly using "primitive database functions" which he found made his life as a teacher, deputy principal (relieving) 
              and then director of the Queen Elizabeth Night School in Palmerston North far easier as he got to grips with payrolls, spreadsheets and other 
              business-based functions."""
tokens = nltk.word_tokenize(passage)
posTags = nltk.pos_tag(tokens)

wantedTag = set(['NN', 'NNS', 'NNP', 'NNPS'])
wantedWord = []
for word, pos in posTags:
       if(pos in wantedTag):
              wantedWord.append(word)
              print(word)
