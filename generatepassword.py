import random
import string

## Global Variables ##
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_characters = "!#%$&^?@"
amount = 1 ## Amount of passwords generated ##

upper, lower, numbers, symbols = True, True, True, True ## Enables all character types ##

passGen = ""
try:
    passLength = int(input("Password character length (Max: 70): ")) ## User input to determine password length ##
except ValueError:
    raise SystemExit("Only numerical values")
except NameError:
    raise SystemExit("Only numerical values")


## Adding characters to password ##
if upper:
    passGen += uppercase_letters
if lower:
    passGen += lowercase_letters
if numbers:
    passGen += digits
if symbols:
    passGen += special_characters
## Generating password ##
try:
    for x in range(amount):
        password = "".join(random.sample(passGen, passLength))
        print(password)
except ValueError:
    print("Password length must be under 70 characters.")
