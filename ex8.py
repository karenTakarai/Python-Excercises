#assign 4 empty spaces to the variable formatter
formatter = "{} {} {} {}"

#show the variable formatter filling their spaces with values 1,2,3 and 4
print(formatter.format(1, 2, 3, 4))
#show the variable fomtatter filling their spaces with values "one", "two", "three" and "four"
print(formatter.format("one", "two", "three", "four"))
#show the variable fomratter filling their spaces with values True, False, True and False
print(formatter.format(True, False, True, False))
#show the variable formatter filling their spaces with the same formatter variable
print(formatter.format(formatter, formatter, formatter, formatter))
#show the formatter variable filling their spaces with "Try your", "Own text here", "Maybe a poem" and "Or a song about fear"
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

#---------------------------------------------------------------------------------------------------------->
#Broken and Fixed code
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
