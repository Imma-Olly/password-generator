import random
import array
 
# maximum length of password needed
MAX_LEN = 8
 
# Declaring arrays of the characters needed
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOWERCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
UPPERCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

#Combine all the characters into one array
COMBINED_LIST = DIGITS + UPPERCASE_CHARACTERS + LOWERCASE_CHARACTERS + SYMBOLS
 
# Randomly select any of the characters
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPPERCASE_CHARACTERS)
rand_lower = random.choice(LOWERCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
 
#Combine the randomly selected characters
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
 
 
for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
 
    # convert temporary password into array and shuffle to
    # prevent it from having a consistent pattern
    # where the beginning of the password is predictable
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
 
# traverse the temporary password array and append the chars
# to form the password
password = ""
for x in temp_pass_list:
        password = password + x
         
# print out password
print(password)