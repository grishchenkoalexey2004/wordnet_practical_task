#Вычисляет количество пар слов из word_pairs.txt связанных соотношением гипоним - гипероним (ответ - 2)

#Вывод: все пары слов связанные отношением гипоним-гипероним + количество пар + среднее значение близости слов в этих парах
# Ответ: 59 пар, среднее значение близости : 6.59

import nltk
from statistics import mean
from nltk.corpus import wordnet as wn


data_file = "word_pairs.txt"
word_pairs = []
proximities = []

with open(data_file,'r') as data:
    for line in data:
        relation,word1,word2,proximity = line.split()
        word_pairs.append([word1,word2,float(proximity)])
    

# retrieves the set of synsets representing unique hyponyms for argument synset using recursive search
def get_hyponyms(synset):
    hyponyms = set()
    for hyponym in synset.hyponyms():
        hyponyms |= set(get_hyponyms(hyponym))
    return hyponyms | set(synset.hyponyms())


def has_hyponym_relation(wordpair):

    #checking whether wordpair[1] is hyponym of wordpair[0] 
    word1_synset_list = wn.synsets(wordpair[0])
    word2_synset_list = wn.synsets(wordpair[1])

    for word1_synset in word1_synset_list:
        synset_hyponyms = get_hyponyms(word1_synset) 
        intersection = set(word2_synset_list) & synset_hyponyms
        if (len(intersection)!=0):
            print("{} is hyponym of {}".format(wordpair[1],wordpair[0]))
            proximities.append(wordpair[2])
            return True 
    # if wordpair[1] is already found in the list of hyponyms for some synset, 
    #there is no need to continue searching

    #checking whether wordpair[0] is hyponym of wordpair[1] 
    for word2_synset in word2_synset_list:
        synset_hyponyms = get_hyponyms(word2_synset)
        intersection = set(word1_synset_list) & synset_hyponyms
        if (len(intersection)!=0):
            print("{} is hyponym of {}".format(wordpair[0],wordpair[1]))
            proximities.append(wordpair[2])
            return True 
        
    return False

result = 0


for pair in word_pairs:
    if (has_hyponym_relation(pair)):
        result+=1


print("Количество пар связанных отношением гипоним-гипероним:{}".format(result))
print("Среднее значение близости: {}".format(mean(proximities)))
    
