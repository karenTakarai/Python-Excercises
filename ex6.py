#assign a value (int) to types_of_people variable
types_of_people = 10
#set a string and insert a variable in it
x = f"there are {types_of_people} type of people."

#assign a value (string) to binary variable
binary = "binary"
#assign a value (string) to do_not variable
do_not = "don't"
#assign a value (string) with embedded variables to y variable
y = f"Those who know {binary} and those who {do_not}" #(1) y (2)

#Show "There are 10 types of people"
print(x)
#Show "Those who know binary and those who don't"
print(y)

#show "There are 10 types of people"
print(f"I said: {x}") #(3)
#show "'Those who know binary and those who don't'"
print(f"I also said: '{y}'") #(4)

#assign false to hilarious variable
hilarious = False
#assign "Isn't that joke so funny?" to joke_evaluation variable
joke_evaluation = "Isn't that joke so funny?! {}"

#show "Isn't that joke so funny?! False"
print(joke_evaluation.format(hilarious))

#assign value (string) to w variable
w = "This is the left side of..."
#assign vale (string) to w variable
e = "a string with a right side."

#show "This is the left side of..." and add "a string with a right side"
print(w + e) #(5) (6)

#----------------------------------------------------------------------------------------->
#Break code -- fixed 

types_of_people = 10
x = f"there are {types_of_people} {y} type of people."

binary = "binary" 
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y + w)

print(f"I said: {x}") #(3)
print(f"I also said: '{y}'") #(4)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)