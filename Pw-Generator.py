import random
import string

def passwordGenerator(lenght, numbers=False, specials=False):
    # extrak the element that need from string module
    letters = string.ascii_letters
    digits = string.digits
    spesial = string.punctuation

    #combine all of element (letters is must but another wait feedback from user)
    combine = letters
    if numbers:
        combine += digits
    if specials:
        combine += spesial

    #variable to storage the random password
    pw = ''

    #while looping to suffle and making the password
    while len (pw) < lenght:
        suffle = random.choice(combine)
        pw += suffle
        #when pw contain a number, number will not adding 
        if pw in digits:
            numbers = False
        #when pw contain a special character, it will not adding
        elif pw in spesial:
            specials = False
    #show the result of password generator
    print (pw)

#ask user to enter a lenght of password
user_lenght = int(input('Enter Lenght of The Password: '))
#user must enter number more than 4 (minimum lenght of password)
if user_lenght < 4:
    print ('The Password Must More Than 4 !')
    exit ()
#ask user to add number and special character into the password or not
user_number = input('Do you want to insert number to the password (y/n): ').upper() == "Y"
user_special = input('Do you want to insert special character to the password (y/n): ').upper() == "Y"

passwordGenerator(user_lenght, user_number, user_special)
