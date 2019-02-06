#create a function with 2 arguments which will be shown
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for party!")
    print("Get a blanket. \n")

#call the function passing numbers directly as arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#call the function passing variables as arguments
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#call the function passing math operation as arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#call the function passing math operations and variables combinated
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#----------------------------------------------------------------------->
#Study Drills

def myFunction(first, second):
    result = first * second
    print(f"the product of {first} X {second} is {result}")

myFunction(10, 15)

factor1 = 236
factor2 = 78
myFunction(factor1, factor2)

myFunction(factor1 - 100, factor2 + 50)