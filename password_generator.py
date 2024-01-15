import random
import string

def generated_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if special_characters:
            meets_criteria = meets_criteria and has_special
    
    return password


min_length = int(input('Enter minimum length: '))
has_numbers = input("Would you like to include a number (y/n)? ").lower() == "y"
has_special = input("Would you like to include a special character (y/n)? ").lower() == "y"

password = generated_password(min_length, has_numbers, has_special)
print("The generated password is " , password)
            
