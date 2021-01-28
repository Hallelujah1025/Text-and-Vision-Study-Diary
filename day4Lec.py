from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import nltk


# def get_continuous_chunks(text):
#     chunked = ne_chunk(pos_tag(word_tokenize(text)))
#     prev = None
#     continuous_chunk = []
#     current_chunk = []
#     #print(chunked)
#     for i in chunked:
#         if type(i) == Tree:
#             current_chunk.append(" ".join([token for token, pos in i.leaves()]))
#         elif current_chunk:
#             named_entity = " ".join(current_chunk)
#             if named_entity not in continuous_chunk:
#                 continuous_chunk.append(named_entity)
#                 current_chunk = []
#         else:
#             continue
#
#     return continuous_chunk

txt = "Jacinda Ardern is the Prime Minister of New Zealand but Roenzo isn't New Zealand and United States of America."
# print(get_continuous_chunks(txt))


count = {}
words = []
for sent in nltk.sent_tokenize(txt):
   for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
       if hasattr(chunk, 'label'):
           if (' '.join(c[0] for c in chunk)) not in words:
               words.append(' '.join(c[0] for c in chunk))
               if chunk.label() in count:
                   count[chunk.label()] += 1
               else:
                   count[chunk.label()] = 1



print(words)
print(count)


# print(count)
