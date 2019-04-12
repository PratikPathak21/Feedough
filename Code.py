from gensim.models import Word2Vec
import bs4 as bs  
import urllib.request  
import re  
import nltk
from allwordsfile import *
# scrapped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')  
# article = scrapped_data .read()

# parsed_article = bs.BeautifulSoup(article,'lxml')

# paragraphs = parsed_article.find_all('p')

# # #
# article_text=''
# for p in paragraphs:
#     article_text+=p.text
# processed_article = article_text.lower()  
# processed_article = re.sub('[^a-zA-Z]', ' ', processed_article )  
# processed_article = re.sub(r'\s+', ' ', processed_article)
# #print(type(processed_article))
# # Preparing the dataset
# all_sentences = nltk.sent_tokenize(processed_article)
# nltk.download('stopwords')
# all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

# from nltk.corpus import stopwords  
# for i in range(len(all_words)):  

#     all_words[i] = [w for w in all_words[i] if w not in stopwords.words('english')]
#print(all_words)
word2vec= Word2Vec.load("word2vec.model")
#word2vec = Word2Vec(all_words, min_count=1)
# word2vec.save("word2vec.model")
# vocabulary = word2vec.wv.vocab
s=str(input())
try:
    print(word2vec.most_similar(s))
except:
    KeyError
    allwords[0].append(s);
    word2vec=Word2Vec(allwords,min_count=1)
    print(word2vec.most_similar(s))  
    word2vec.save("word2vec.model")
#print(word2vec.most_similar('Knowledge'))














# arr = nltk.sent_tokenize(word)
# arr1=[nltk.word_tokenize(sent) for sent in arr]
# #worddict['s'].append('supernatural')
# print(arr1)
# w2v=Word2Vec(arr1, min_count=1,size=10,seed=1,workers=1)
# vocabulary= w2v.wv.vocab
# v1 = w2v.wv['King']
# print(v1)
# print(w2v.wv.most_similar('King',topn=10))

#print(worddict)
#print(models.similarity('france','spain'))
