import random
import array

#program prompts user for desired length of password and then spits out what the user desires"

pwlen = input('desired length of password? ')
uppercasebool = input('uppercase letters in password? y/n: ')    
lowercasebool = input('lowercase letters in password? y/n: ')
digitbool = input('numbers in password? y/n: ')
symbolbool = input('symbols in password? y/n: ')

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

combinedselect = []

if uppercasebool == 'y':
    combinedselect = combinedselect + uppercase

if lowercasebool == 'y':
    combinedselect = combinedselect + lowercase

if digitbool == 'y':
    combinedselect = combinedselect + numbers

if symbolbool == 'y':
    combinedselect = combinedselect + symbols

password = ""

for i in range(int(pwlen)):
    password = password + random.choice(combinedselect)

print(password)

