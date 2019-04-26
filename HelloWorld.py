#Hello World 

print('Hello, Python!')

# Check the Python Version

import sys
print(sys.version)

#Two types of error :  NameError and SyntaxError

#1. Data Types

## Python refers to integers as int, floats as float, and character strings as str
##Type() permet de connaitre le type d'objet

##Learn the specifics of floats for your runtime environment, by checking the value of sys.float_info. This will also tell you what's the ##largest and smallest number that can be represented with them.

sys.float_info

## Convert 2 to a float

float(2)

## Convert integer 2 to a float and check its type

type(float(2))

## Casting 1.1 to integer will result in loss of information

int(1.1)

## Convert a string into an integer

int('1')

## Convert a string into an integer with error

int('1 or 2 people')

## strings can be represented with single quotes ('1.2') or double quotes ("1.2")

## An object of type Boolean can take on one of two values: True or False. "bool"

#2. Expressions

## Integer division operation expression

25 // 5

#3. Variables

# Store value into variable

x = 43 + 60 + 16 + 41


