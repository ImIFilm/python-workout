from random import randint
import random
import json
from pprint import pprint

path = '/Users/ImI/pkedzior/slowa.txt' #sciezka do pliku ze slowami
path2 = '/Users/ImI/pkedzior/slowa.json' #sciezka2 do pliku ze slowami

#funkcja, ktora generuje jakis randomowy string
def create_random_string():
    s = "abecudpk"
    passlen = 4
    p =  "".join(random.sample(s,passlen))
    p+=" "
    return p

#funkcja ktora losuje slowo z pliku
def take_one_word(this_path):
    try:
        data=json.load(open('slowa.json'))
        amount_of_words = 0
        defi, question_w = random.choice(list(data.items()))
        print ("\nPODPOWIEDZ: ", defi)
        #print ("HASLO: ", question_w)
    except FileNotFoundError:
        print ("Pliku nie ma, wiec wygeneruje jakies haslo")
        question_w=create_random_string()
    except ValueError:
        print ("Plik jest pusty, wiec wygeneruje jakies haslo")
        question_w=create_random_string()
    return question_w


question_word=take_one_word(path2)

#print (question_word) #losuje cos randomowego
word_len = len(question_word) #dlugosc stringa

print ("WITAJ, TWOJE SŁOWO MA ", word_len, "LITER")
correct=0 #czy mamy juz odpowiedz
wrong_letter=0 #ile razy podalismy zla literke
my_list=[]
for i in range (0,word_len):
    my_list.append("_")

while (correct==0):
    print ("\nilosc zlych trafien:", wrong_letter )
    if (wrong_letter>3):
        print ("ZA DUZO WPADEK! Wylatujesz!")
        quit()
    print (' '.join(my_list))
    tmp_letter = input("Podaj literke: ")
    print ("WCZYTANO: ", tmp_letter)
    exists=0
    for i in range (0,word_len):
        if (tmp_letter==question_word[i]):
            my_list[i]=tmp_letter
            exists=1
    if (exists==0):
        wrong_letter=wrong_letter+1
    var=0
    for i in range (0,word_len):
        if (my_list[i]=="_"):
            var=var+1
    if (var==0):
        correct=1
print ("\nWYGRAŁEŚ!\n", ' '.join(my_list))