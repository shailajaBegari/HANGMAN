import random
import string
from words import choose_word
from image import IMAGES
secret_word=choose_word()
def ava_let(l_g):
  letters_left=string.ascii_lowercase
  ava_let=""
  for l in letters_left:
    if l not in l_g:
      ava_let+=l
  return ava_let
def get_guessed_word(s,l_g):
  i=0
  guessed_word=""
  while i<len(s):
    if s[i] in l_g:
      guessed_word+=(s[i])
    else:
      guessed_word+=("_")
    i=i+1
  return guessed_word
def is_word_guessed(s,l_g):
  if s==get_guessed_word(s,l_g):
    return True
  return False
def ifvalid(letter):
  if len(letter)!=1:
    return False
  if not letter.isalpha():
    return False
  return True
def get_hint(l_g,s):
  l_n_g=[]
  for i in s:
    if i not in l_g:
      if i not in l_n_g:
        l_n_g.append(i)
  return(l_n_g[0])

def hangman():
  print(secret_word)
  name=input("enter your name= ")
  print("Welcome to Hangman Game ",name, "\U0001F917")
  print("Try to guess the word   ")
  print("_ _ _ _ _",name,"\U0001F618"," _ _ _ _ _ _ _")
  print("I am thinking of a word that is " , str(len(secret_word)) , " letters long.")
  print("")
  level=input("enter the level u want a/Easy b/Medium, c/Hard:")
  if level=="a":
    image_index=[0,1,2,3,4,5,6,7]
    remaining_lives=8
  elif level=="b":
    image_index=[0,2,4,5,6,7]
    remaining_lives=6
  elif level=="c":
    image_index=[0,2,4,6]
    remaining_lives=4
  i=0
  letters_guessed = []
  list=[]
  hint=0
  while remaining_lives>0:
    available_letters = ava_let(letters_guessed)
    print("Available letters: " , available_letters)
    guess = input("Please guess a letter: ")
    letter = guess.lower()
    if guess=="hint":
      if hint==0:
        print("ur next word is:",get_hint(letters_guessed,secret_word))
      else:
        print("ur alredy used hint")
      hint+=1

    if ifvalid(guess)==False:
      continue
    if guess not in ava_let(letters_guessed):
      continue
    if letter in secret_word:
      letters_guessed.append(letter)
      list.append(letter)
      print(list)
      print("Good guess: " ,get_guessed_word(secret_word, letters_guessed))
      print(" ")
      if is_word_guessed(secret_word, letters_guessed) == True:
        print(" * * Congratulations, you won! * * ")
    else:
      ava_letters=ava_let(letters_guessed)
      print("Oops! That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
      print (IMAGES[image_index[i]])
      letters_guessed.append(letter)
      remaining_lives -= 1
      print ("Remainking Lives : ", remaining_lives)
      i=i+1
    if remaining_lives<=0:
      print("you ran out of this game:",secret_word)
hangman()

    
