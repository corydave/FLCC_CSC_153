# FILE NAME - password.py

# NAME: Jasmine Allen
# DATE: 2.14.24
# BRIEF DESCRIPTION:  Password Lab



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random
import string

def main():
    generate_password()

def generate_password():

  
    ########## ENTER YER CODE BELOW THIS LINE ##########

    user_seed = int(input('Enter a seed for the random number generation: '))
    random.seed(user_seed)

    print('hi')

    special_character = random.choice("!, @, #, $, &, (, ), ,, -, _, ")
    lower_case = random.choice(string.ascii_lowercase)
    upper_case = random.choice(string.ascii_uppercase)
    number = random.choice(string.digits)

    print("Your random password is: ")
    print(f"{special_character}{lower_case}{upper_case}{lower_case}{upper_case}{number}{number}{special_character}")

main()





    ########### END YER CODE ABOVE THIS LINE ###########