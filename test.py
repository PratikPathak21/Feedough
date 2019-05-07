import nltk
from nltk.corpus import wordnet as wn
from itertools import chain	
import re
from random import *
print("Choose your Industry")
print("1. Food and Beverages")
print("2. Technology")
print("3. Finance")
print("4.Manufacturing")
print("5.Automotive")
print("6.Beauty")
print("7.Kids")
print("8.Fashion")
print("9.Social/Environment")
print("10.Delivery/storage 11.IT/Software/SAAS 12.Restaurants & Food Service 13.Hospitality 14.Communication 15.Creative 16.Entertainment 17.Education 18.Banking/Finance 19.Health 20.Gaming 21.Tourism 22.Delivery Party / Clubbing")

arr=[['rew','ice','king','star','azy','asy','ol'],
['stat','ster','tron','urgy','ware','scop'],
['1Accu','1Tap','up','ye','1bright','1cred','0easy','0ez','1crypt','1secur','tru','1TRUE','trust','one','ezy','vest','raph','afe'],
['gear','gauge','tool','man','1Auto','one','ace'],
['1pro','1auto','1mech','shop','1moto','1play','1exper','0flex','0go','ero'],
['glam','shine','pure','express','studio','ious','ish','1perfect','box','1genic'],
['0care','1club','0smart','1clever','plus','pal','bee','crate'],
['art','style','tren','sharp','smooth','dept','ranch','wear','glam','1hello','you','love','society','club','look','mark','dresses'],
['hand','help','1hello','steps','care','keeper','1keep','1protect','1watch'],
['ly','io','xio','ing','age','ic','ick']]

temp1=[]

prefixes=list(map(str,"anti de dis em en fore il im im in in inter ir mid mis non over pre re semi sub super trans un under".split()))
suffixes=list(map(str,"able able age al al al ance ant ar ate ate ation ative ed ed ee en en ence ent eous er er er er es ese ess est est ette ful ful fully hood ial ible ible ic ic ical ice ing ing ion ious ise ish ism ist ition itive ity ive ive ize less less let ly ly ment ment ness ness or or ous ous s sion some tain tion tion ty ure wards ways wide wise worthy y yze".split()))

# print(prefixes)
# print(suffixes)
def sylco(word) :

    word = word.lower()

    # exception_add are words that need extra syllables
    # exception_del are words that need less syllables

    exception_add = ['serious','crucial']
    exception_del = ['fortunately','unfortunately']

    co_one = ['cool','coach','coat','coal','count','coin','coarse','coup','coif','cook','coign','coiffe','coof','court']
    co_two = ['coapt','coed','coinci']

    pre_one = ['preach']

    syls = 0 #added syllable number
    disc = 0 #discarded syllable number

    #1) if letters < 3 : return 1
    if len(word) <= 3 :
        syls = 1
        return syls

    #2) if doesn't end with "ted" or "tes" or "ses" or "ied" or "ies", discard "es" and "ed" at the end.
    # if it has only 1 vowel or 1 set of consecutive vowels, discard. (like "speed", "fled" etc.)

    if word[-2:] == "es" or word[-2:] == "ed" :
        doubleAndtripple_1 = len(re.findall(r'[eaoui][eaoui]',word))
        if doubleAndtripple_1 > 1 or len(re.findall(r'[eaoui][^eaoui]',word)) > 1 :
            if word[-3:] == "ted" or word[-3:] == "tes" or word[-3:] == "ses" or word[-3:] == "ied" or word[-3:] == "ies" :
                pass
            else :
                disc+=1

    #3) discard trailing "e", except where ending is "le"  

    le_except = ['whole','mobile','pole','male','female','hale','pale','tale','sale','aisle','whale','while']

    if word[-1:] == "e" :
        if word[-2:] == "le" and word not in le_except :
            pass

        else :
            disc+=1

    #4) check if consecutive vowels exists, triplets or pairs, count them as one.

    doubleAndtripple = len(re.findall(r'[eaoui][eaoui]',word))
    tripple = len(re.findall(r'[eaoui][eaoui][eaoui]',word))
    disc+=doubleAndtripple + tripple

    #5) count remaining vowels in word.
    numVowels = len(re.findall(r'[eaoui]',word))

    #6) add one if starts with "mc"
    if word[:2] == "mc" :
        syls+=1

    #7) add one if ends with "y" but is not surrouned by vowel
    if word[-1:] == "y" and word[-2] not in "aeoui" :
        syls +=1

    #8) add one if "y" is surrounded by non-vowels and is not in the last word.

    for i,j in enumerate(word) :
        if j == "y" :
            if (i != 0) and (i != len(word)-1) :
                if word[i-1] not in "aeoui" and word[i+1] not in "aeoui" :
                    syls+=1

    #9) if starts with "tri-" or "bi-" and is followed by a vowel, add one.

    if word[:3] == "tri" and word[3] in "aeoui" :
        syls+=1

    if word[:2] == "bi" and word[2] in "aeoui" :
        syls+=1

    #10) if ends with "-ian", should be counted as two syllables, except for "-tian" and "-cian"

    if word[-3:] == "ian" : 
    #and (word[-4:] != "cian" or word[-4:] != "tian") :
        if word[-4:] == "cian" or word[-4:] == "tian" :
            pass
        else :
            syls+=1

    #11) if starts with "co-" and is followed by a vowel, check if exists in the double syllable dictionary, if not, check if in single dictionary and act accordingly.

    if word[:2] == "co" and word[2] in 'eaoui' :

        if word[:4] in co_two or word[:5] in co_two or word[:6] in co_two :
            syls+=1
        elif word[:4] in co_one or word[:5] in co_one or word[:6] in co_one :
            pass
        else :
            syls+=1

    #12) if starts with "pre-" and is followed by a vowel, check if exists in the double syllable dictionary, if not, check if in single dictionary and act accordingly.

    if word[:3] == "pre" and word[3] in 'eaoui' :
        if word[:6] in pre_one :
            pass
        else :
            syls+=1

    #13) check for "-n't" and cross match with dictionary to add syllable.

    negative = ["doesn't", "isn't", "shouldn't", "couldn't","wouldn't"]

    if word[-3:] == "n't" :
        if word in negative :
            syls+=1
        else :
            pass   

    #14) Handling the exceptional words.

    if word in exception_del :
        disc+=1

    if word in exception_add :
        syls+=1     

    # calculate the output
    return numVowels - disc + syls
ansarr=[]


def wordcombiner(addarr,temp1):

    k=len(ansarr)
    for i in range(0,len(addarr)):
        ansarr.append(addarr[i]+addarr[i][-1])
        ansarr.append(addarr[i][0]+addarr[i])
    #suffix-prefix add
    k=len(ansarr)
    for i in range(len(temp1)):
        for j in range(len(addarr)):
            if(temp1[i][0]=='1'):
                ansarr.append(temp1[i][1:]+addarr[j])
            elif(temp1[i][0]=='0'):
                ansarr.append(addarr[j]+temp1[i][1:])
                ansarr.append(temp1[i]+addarr[j][1:])
            else:
                ansarr.append(addarr[j]+temp1[i])
    
    # for j in range(26):
    # 	for i in range(len(arr)):
    # 		ansarr.append()
    syllablecount=[]
    for i in range(len(ansarr)):
        syllablecount.append(sylco(ansarr[i]))

    k=len(ansarr)
    for i in range(k):
        if(syllablecount[i]<=3):
        	for j in range(len(suffixes)):
        		ansarr.append(ansarr[i]+suffixes[j])
        	for j in range(len(prefixes)):
        		ansarr.append(prefixes[j]+ansarr[i])

    #print(*syllablecount)

def generator(wordlist,typ):
	
    for word in wordlist:
        synonyms = [] 
        hyponyms = []
        final = []
        temp1=arr[typ]+arr[-1]
        for i,j in enumerate(wn.synsets(word)):
    		#print(i,j)
            for I in list(chain(*[l.lemma_names() for l in j.hyponyms()])):
                hyponyms.append(I)

        for syn in wn.synsets(word):
            for l in syn.lemmas():
                synonyms.append(l.name()) 
        #if l.antonyms(): 
        #    antonyms.append(l.antonyms()[0].name()) 
        p = list(set(hyponyms + synonyms))
        #print(p)
        wordcombiner(p,temp1)
    shuffle(ansarr)
    print(ansarr)

	# temp1=arr[typ]+arr[-1]
	# synonyms = [] 
	# hyponyms = []
	# final = []
	# for i,j in enumerate(wn.synsets(word)):
	# 	for I in list(chain(*[l.lemma_names() for l in j.hyponyms()])):
 #  			hyponyms.append(I)

	# for syn in wn.synsets(word):
	# 	for l in syn.lemmas():
	# 		synonyms.append(l.name()) 
 #        #if l.antonyms(): 
 #        #    antonyms.append(l.antonyms()[0].name()) 
	# p = list(set(hyponyms + synonyms))
	
	# for i in range(len(temp1)):
	# 	for j in range(len(p)):
	# 		result.append(p[j]+temp1[i])

	# print(result)


a=int(input())
print("Enter keywords in a single line seperated by spaces: ")
keyword=list(map(str,input().split()))

generator(keyword,a-1)

# result=[]
# print(len(temp1))
# for i in range(len(arr[a-1])+len(arr[-1])):
# 	for j in range(len(p)):
# 		result.append(p[j]+temp1[i])
# print(result)


# if a==1:
# 	result=[]
	
# 	a=input()
# 	temp1=foodandbeverages+common
	
	
# 	if(len(p)<10):

	

# 	print(result)

# if a==2:
# 	result=[]
# 	print("Enter a keyword : ")
# 	a=input()

# 	# idhar loop chalake synonym ka utha aur foodbeverages & common se seedha concatenate karke result main
# 	temp1=Technology+common
# 	synonyms = [] 
# 	hyponyms = []
# 	final = []
# 	for i,j in enumerate(wn.synsets(a)):
# 		for I in list(chain(*[l.lemma_names() for l in j.hyponyms()])):
#   			hyponyms.append(I)

# 	for syn in wn.synsets(a):
# 		for l in syn.lemmas():
# 			synonyms.append(l.name()) 
#         #if l.antonyms(): 
#         #    antonyms.append(l.antonyms()[0].name()) 
# 	p = list(set(hyponyms + synonyms))
# 	for i in range(len(temp1)):
# 		for j in range(len(p)):
# 			result.append(p[j]+temp1[i])

# 	print(result)

# if a==3:
# 	result=[]
# 	print("Enter a keyword : ")
# 	a=input()

# 	# idhar loop chalake synonym ka utha aur foodbeverages & common se seedha concatenate karke result main
# 	temp1=Finance+common
# 	synonyms = [] 
# 	hyponyms = []
# 	final = []
# 	for i,j in enumerate(wn.synsets(a)):
# 		for I in list(chain(*[l.lemma_names() for l in j.hyponyms()])):
#   			hyponyms.append(I)

# 	for syn in wn.synsets(a):
# 		for l in syn.lemmas():
# 			synonyms.append(l.name()) 
#         #if l.antonyms(): 
#         #    antonyms.append(l.antonyms()[0].name()) 
# 	p = list(set(hyponyms + synonyms))
# 	for i in range(len(temp1)):
# 		for j in range(len(p)):
# 			result.append(p[j]+temp1[i])

# 	print(result)
			
