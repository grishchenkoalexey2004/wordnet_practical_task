# Вычисляет, сколько пар слов из word_pairs.txt связано отношением (часть-целое)

#Вывод: пары слов связанных отношением часть-целое + количество пар + среднее значение близости слов в этих парах

#Ответ: 4 пары

import nltk
from nltk.corpus import wordnet as wn
from statistics import mean

data_file = "word_pairs.txt"
word_pairs = []
proximities = [] 

result = 0

with open(data_file,'r') as data:
    for line in data:
        relation,word1,word2,proximity = line.split()
        word_pairs.append([word1,word2,float(proximity)])
    



# returns a set of meronyms for synset
def get_meronyms(synset):
    meronyms = set()
    for part_meronym in synset.part_meronyms():
        meronyms |= set(get_meronyms(part_meronym))

    for substance_meronym in synset.substance_meronyms():
        meronyms |= set(get_meronyms(substance_meronym))

    meronyms |=set(synset.part_meronyms())
    meronyms |= set(synset.substance_meronyms())

    return meronyms



def has_meronym_relation(wordpair):

    #checking whether wordpair[1] is hyponym of wordpair[0] 
    word1_synset_list = wn.synsets(wordpair[0])
    word2_synset_list = wn.synsets(wordpair[1])

    for word1_synset in word1_synset_list:
        synset_meronyms = get_meronyms(word1_synset) 
        intersection = set(word2_synset_list) & synset_meronyms
        if (len(intersection)!=0):
            print("{} is meronym of {}".format(wordpair[1],wordpair[0]))
            proximities.append(wordpair[2])
            return True 
    # if wordpair[1] is already found in the list of hyponyms for some synset, 
    #there is no need to continue searching

    #checking whether wordpair[0] is hyponym of wordpair[1] 
    for word2_synset in word2_synset_list:
        synset_meronyms = get_meronyms(word2_synset)
        intersection = set(word1_synset_list) & synset_meronyms
        if (len(intersection)!=0):
            print("{} is meronym of {}".format(wordpair[0],wordpair[1]))
            proximities.append(wordpair[2])
            return True 
        
    return False



for pair in word_pairs:
    if (has_meronym_relation(pair)):
        result+=1

print("Количество пар связанных отношением часть-целое:{}".format(result))
print("Среднее значение близости: {}".format(mean(proximities)))


