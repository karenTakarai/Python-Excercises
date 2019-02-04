#show a string and avoid the line end with a new line
print("How old are you", end=' ')
#get the answer of the user and save it in the age variable
age = input()
#show a string and avoid the line end with a new line
print("how tall are you?", end=' ')
#get the answer of the user and save it in the height variable
height = input()
#show a string and avoid the line end with a new line
print("How much do you weigh?", end=' ')
#get the answer of the user and save ir in the weight variable
weight = input()

#show a string with the answers of the user.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#--------------------------------------------------------------------->
#Broken and Fixed Code

print("How old are you", end=' ')
age = input()
print("how tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = int(input())

print(f"So, you're {age} old, {height} tall and {weight + weight} heavy.")
#other form------------------------------------------------------------>
age = int(input("How old are you? "))
height = input("how tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age + age} old, {height} tall and {weight} heavy.")
