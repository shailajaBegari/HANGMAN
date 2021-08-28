import random
def load_words():
    f=open("words.txt","r")
    data=f.read().split() 
    empty=[]
    for word_list in data:
        empty.append(word_list)
    return empty
def choose_word():
    empty = load_words()
    secret_word = random.choice(empty)
    secret_word = secret_word.lower()
    return secret_word
