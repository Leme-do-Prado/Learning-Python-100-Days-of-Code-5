import random
import string

print("Hi! Welcome to the password generator \n I'm going to ask you a few questions now.")

amount_of_letters = int(input("What's the desired amount of letters? Type in.\n"))
amount_of_numbers = int(input("What's the desired amount of numbers? Type in.\n"))
amount_of_symbols = int(input("What's the desired amount of symbols? Type in.\n"))

char = ""
char_list = list(char)


for letter in range(1, amount_of_letters+1):
    char = random.choice(string.ascii_letters)
    char_list.append(char)

for number in range(1, amount_of_numbers+1):
    char = random.choice(string.digits)
    char_list.append(char)

for symbol in range(1, amount_of_symbols+1):
    char = random.choice(string.punctuation)
    char_list.append(char)

random.shuffle(char_list)

password = "".join(char_list)
print(password)
