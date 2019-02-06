from sys import argv

#get the arguments and assign to script variable and filename variable
script, filename = argv

#create a file object of the file which is specified in the filename variable and save ir in txt variable.
txt = open(filename)

#show the filename variable
print(f"Here's your file {filename}:")
#Read the text of the file through the txt variable
print(txt.read())
#Close the file
txt.close()

#Prompt the path of a new file and save it in the file_again
print("Type the filename again:")
file_again = input("> ")

#open the file and create a file object
txt_again = open(file_again)

#Read the text of the file through the txt variable
print(txt_again.read())
#Close the second file
txt_again.close()