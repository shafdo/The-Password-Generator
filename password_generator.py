import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
numbers = string.digits
special = string.punctuation

all_char = list(upper+lower+numbers+special)

print("""\n         Tip: Try to grab a password which has 8 or more characters 
                      to make your password more secure...
			    by yugantha shalinda
\n""")

def passwd(all_char):
    running = True
    userdec1= int(input("\033[1;31mEnter password lenght: \033[1m"))
    password = random.sample(all_char,userdec1)
    password = ''.join(password)
    print(password)
    
    while running:
        userdec2 = input("Do you want a different password y/n: ")
        if userdec2 == "y":
            password = random.sample(all_char,userdec1)
            password = ''.join(password)
            print(password)
        else:
            running = False
            print("\n                   Your password is:   "+password)
            print('''\033[1;34m
            Thank you For trying the password generator
            \033[1m''')


passwd(all_char)
