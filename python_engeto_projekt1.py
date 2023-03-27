"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author:Marcel Halamka
email: maacek1@seznam.cz
discord: Kronos#8011
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

user = input("Hello what is your name:\n")
password = input("Write your password:\n")
separator = 40*"-"
 
if user in users and users[user] == password:
    print(separator)
    print(f"Welcome to the app, {user}\nWe have {len(TEXTS)} texts to be analyzed.")
    print(separator)
else:
    print(f"username:{user}\npassword:{password}")
    print("unregistered user, terminating the program..")
    quit()

#Choosing text
part = input(f"Enter a number btw. 1 and {len(TEXTS)} to select:\n")
if part.isdigit():
    part = int(part)
    if part >= 1 and part <= 3:
        pass
    else:
        print("No available!!Terminating the program...")
        quit()
else:
    print("No available!!Terminating the program...")
    quit()
print(separator)
lst_words = TEXTS[part-1].split()

#Total words
print(f"There are {len(lst_words)} words in the selected text.")

#Total titlecase
total_titlecase = 0
for word in lst_words:
    if word.istitle():
        total_titlecase += 1
print(f"There are {total_titlecase} titlecase words.")

#Total uppercase(without numbers in string)
total_upper = 0
for word in lst_words:
    if word.isupper() and word.isalpha():
        total_upper += 1
print(f"There are {total_upper} uppercase words.")


#Total lowercase
total_lower = 0
for word in lst_words:
    if word.islower():
        total_lower += 1
print(f"There are {total_lower} uppercase words.")

#Total numeric
total_numeric = 0
for word in lst_words:
    if word.isnumeric():
        total_numeric += 1
print(f"There are {total_numeric} numeric strings.")

#Sum of all numbers
sum_numbers = sum([int(word) for word in lst_words if word.isnumeric()])
print(f"The sum of all the numbers {sum_numbers}")

#Occurance
clean_words = [word.strip(",.:;'") for word in lst_words]
print(separator)

occur_list = {}
for word in clean_words:
    length_word = len(word)
    if length_word not in occur_list:
        occur_list[length_word] = 1
    else:
        occur_list[length_word] += 1
sorted_numbers = sorted(occur_list, key = occur_list.get)

#Table
star = "*"
my_len = "LEN"
occurance = "OCCURANCES"
nr = "NR."
print(f"{my_len.rjust(2)}|{(occurance).center(18)}|{nr}", sep="\n")
print(separator)
for index, number in enumerate(sorted(sorted_numbers), 1):
    print(f"{(str(index)).rjust(3)}|{(occur_list[number] * star).ljust(18)}\
        |{occur_list[number]}", sep="\n")

 


    
    







    






