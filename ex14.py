from sys import argv

script, user_name, nick_name = argv
prompt = 'mmh '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"I'd like to ask you few question.")

print(f"first do you prefer i call you {user_name} or {nick_name}?")
name = input(prompt)

print(f"Do you like me {name}")
likes = input(prompt)

print(f"Where do you live {name}?")
lives = input(prompt)

print(f"What kind of computer do you have")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")