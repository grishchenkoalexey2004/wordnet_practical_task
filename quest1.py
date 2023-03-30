# Вычисляет сколько пар слов из word_pairs.txt являются синонимами и выводит эти пары на экран (если они есть)

# Вывод: все синонимичные пары + их количество + среднее значение близости слов в этих парах
# Ответ: 8 пар, среднее значение близости : 8.77

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
    

syn_count = 0


for pair in word_pairs:
    syn_matr = wn.synonyms(pair[0])
    
    for syn_list in syn_matr:
        if (pair[1] in syn_list):
            syn_count+=1
            print("{} - {}".format(pair[0],pair[1]))
            proximities.append(pair[2]) 
            break


print("Количество синонимичных пар: {}".format(syn_count))
print("Среднее значение близости: {}".format(mean(proximities)))


    