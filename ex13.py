from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv

ft = input(f"what do you think about {first}? ")
sd = input(f"now explain what you know about {second}? ")
td = input(f"very interesting, can you tell more about {third}? ")

print(f"""
so you said 
{first} {ft}, 
{second} {sd} and 
{third} {td}
""")