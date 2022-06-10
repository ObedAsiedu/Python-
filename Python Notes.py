#!/bin/python3

#Importing
print("Importing is important:")

import sys #system function and parameters 

from datetime import datetime
print(datetime.now())
 
from datetime import datetime as dt #importing with an alias
print(dt.now())
 
def new_line():
 	print('\n')
 	
new_line()
 
#Advanced Strings
print ("Advanced Strings:")
my_name = "Health"
print(my_name[0]) #first initial
print(my_name[-1]) #last letter

sentence = ("This is a sentence:")

print(sentence[:4]) #first word
print(sentence[-9:-1]) #last word

print(sentence.split()) #split sentence by delimiter (space)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))

quoteception = "I said, 'give me all the money'"
print(quoteception)

quoteception = "I said, \"give me all the money\""
print(quoteception)

print ("A" in "Apple") #Boolean
letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #Improved - case insensitive

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower()))

two_much_space = "              helllo			"
print(two_much_space.strip())

full_name = "eath Adams"
print(full_name.replace("eath", "Heath")) #Replace a letter
print(full_name.find("Adams")) #Find where something occured

movie = "The Hangover"
print("My favourite movie is {}.".format(movie)) #Format it automatically 

def favorite_book(title, author):
	fav = "My favorite book is \"{}\", which is written by {}.".format(title,author)
	return fav
	
print(favorite_book("The Great Gatsby","F. Scott Fitzgerald"))

new_line()

#Dictonaries
print("Dictonaries are keys and value:")
drinks = {"white Russians": 7, "Old Fashion": 10, "Lemon Drop": 8, "Buttery Nipple": 6} #drinks is key, price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)

employees["legal"] = ["Mr. Frond"] #add new key: value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]})
print(employees)

drinks['white Russians'] = 8 #TO update
print(drinks)

print(drinks.get("white Russians")) #TO get how much a drink is