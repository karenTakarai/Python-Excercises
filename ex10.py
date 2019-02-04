#assign a string with a tab in it to tabby_cat variable
tabby_cat = "\tI'm tabbed in."
#assign a string with a split in it to persian_cat
persian_cat = "I'm split\non a line"
#assign a string with two backslash in it to backslash_cat
backslash_cat = "I'm \\ a \\ cat"

#assign a paragraph with tabs and brakeline in it to fat_cat variable
fat_cat = """
I'll do a list
\t*cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

#show tabby_cat variable
print(tabby_cat)
#show persian_cat variable
print(persian_cat)
#show backslash cat variable
print(backslash_cat)
#show fat_cat variable
print(fat_cat)
#-------------------------------------------------------------------->
#study drills
line = "-" * 20
paragraph = """
Escape \t| Example
{}
\\\ \t| Example of \\ usage
\\' \t| Example of \' usage
\\" \t| Example of \" usage
\\a  \t| Example of \a usage
\\b \t| Example of \b usage
\\f \t| Example of \f usage
\\n \t| Example of \n usage
\\r \t| Example of \r usage
\\t \t| Example of \t usage
\\u2665 \t| Example of \u2665 usage
\\v \t| Example of \v usage
\\ooo \t| Example of \123 usage
\\xhh \t! Exmaple of \123 usage
""".format(line)

print(paragraph)
#---------------------------------------------------------->
#Broken and Fixed Code
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\d on a line"
backslash_cat = "I'm \\\ a \\ cat"

fat_cat = """
I'll do a list
\ t*cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)