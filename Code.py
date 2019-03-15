from EnglishWords import *
from gensim.models import Word2Vec
worddict={}
for i in words.keys():
	char=i[0]
	try:
		worddict[char].append(i)
	except:
		KeyError
		worddict[char]=[i]
#worddict['s'].append('supernatural')

arr=[]
for i in worddict.keys():
	arr.append(worddict[i])
model=Word2Vec(arr,min_count=1)
print(model.most_similar('supernatural',topn=10))

#print(worddict)
#print(models.similarity('france','spain'))