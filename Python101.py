#1/bin/python3

#Print string
print ("Strings and things: ")
print ("Hello world!")
print ("""Hello, this is a multi-line string!""")
print( "This is"+" a string")

print('\n') #new line

#maths
print("Math time: " )
print (50 + 50) #add
print (50 - 50) #subtract
print (50 * 50) #multiply
print (50 / 50) #divide
print (50 + 50 * 50 / 50 ) #PEMDAS
print (50 ** 2) #exponents
print (50 % 6) #modulo
print (50 // 6) #number without leftover

print('\n') #new line

#Variables & Methods
print("Fun with variables and methods:")
quote = " All is fair in love and war"
print( len(quote)) #length
print(quote.upper()) #uppercase
print (quote.lower()) #lowercase
print(quote.title()) #title

name = "Francis"
age = 22 #int int(29)
gpa = 3.7 #float float(3.7)

print(int(age))
print(int(29.9)) #does not round

print("My name is " + name + " and I am " + str(age) + " years old.")

print('\n') #new line

age += 1 
print(age)

birthday = 1
age += birthday
print(age)

print('\n') #new line

#Functions 

print( "Now, some functions: ")
def who_am_i():
	name ="Francis"
	age = 22
	print("My name is " + name + " and I am " + str(age) + " years old.")
	
who_am_i()

#Adding in parameters
def add_one_hundred(num):
	print (num + 100)
	
add_one_hundred(100)

#add in multiple parameters
def add(x,y):
	print(x + y)
add(7,7)
add(305,207)

#using return
def multiply(x,y):
	return x * y 

print(multiply(7,7))

def square_root(x):
	return x ** .5 
	
print(square_root(64)) 

print('\n') #new line

#Boolean expressions (True or False)

print("Boolean Expressions:")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

#Rational and Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and = (7 > 5) and (5 < 7) #True and True = True
test_or = (7 > 5) or (5 < 7) # True or True = True
test_not = not True # Not True = False

print(test_and) 

print('\n') #new line

#Conditional Statement
print("Contitional Statement:")
def soda(money) :
	if money >= 2:
		return "You've got yourself a soda!"
	else:
		return "No soda for you!"
print(soda(3))
print(soda(1))

def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return " We're getting tipsy"
	elif (age >= 21) and (money < 5):
		return "Come back with more money."
	elif (age < 21) and (money >=5):
		return "Nice try, kid."
	else:
		return " You're too poor and too young"
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))

print('\n') #new line

#Lists

print("List have brackets:")
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[0]) #Numbering starts at zero with Lists
print(movies[0:3]) #From first movie to the 3rd movie
print(movies[1:]) # Printing starting point of one till then 
print(movies[:1]) # Stop at 1
print(movies[-1]) # -1 pulls last number out of the list
print(len(movies)) # How many movies in the lists

movies.append("JAWS") #Adding a new movie
print(movies)

movies.pop() #pop just removes the last number from the list
print(movies)

movies.pop(1)
print(movies)

movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]
person = ["Health", "Jake", "Leah", "Jeff"] # List have care brackets
combined = zip(movies, person) # 
print(list(combined))

#Tuples
print("Tuples have parantheses anc cannot change") #Tuples are list that cannot be modifield / Tuples have paranthesis
grades = ("A", "B", "C", "D", "F")
print(grades[1])

print('\n') #new line

#Looping 
print("For loops - start to finish of iterate: ")
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)
	
print("While loops - Execute as long as True: ")
i = 1
while i < 10: 