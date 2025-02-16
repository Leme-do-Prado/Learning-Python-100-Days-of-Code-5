import random
import string

print("Hi! Welcome to the password generator \n I'm going to ask you a few questions now.")

amount_of_letters = int(input("What's the desired amount of letters? Type in.\n"))
amount_of_numbers = int(input("What's the desired amount of numbers? Type in.\n"))
amount_of_symbols = int(input("What's the desired amount of symbols? Type in.\n"))

char = ""
char_list = list(char)
i = 0
j = 0
k = 0

while i < amount_of_letters:
    char = random.choice(string.ascii_letters)
    char_list.append(char)
    i += 1

while j < amount_of_numbers:
    char = random.choice(string.digits)
    char_list.append(char)
    j += 1

while k < amount_of_symbols:
    char = random.choice(string.punctuation)
    char_list.append(char)
    k += 1

random.shuffle(char_list)

password = "".join(char_list)
print(password)