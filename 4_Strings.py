'''
Anything inside single, double, triple quotes in python is called string
Strings are IMMUTABLE. Meaning they can't be divided. 
String support 
    Indexing 
        Positive 
        Negative 
    Slicing
'''


# POSITIVE INDEXING : When you initialize a string, Py interpreter automatically indexes every single character to a number starting from 0.
# This will help you to access every character through the number.

name = 'Micheal Jackson'
print(name[0])              # M
print(name[1])              # i
print(name[8])              # J
print(name[7])              # <space>
print(name[55])             # Error


# NEGATIVE INDEXING : The auto number to each and every character from backend, given by py interpreter when you initialize a String.

name = 'Micheal Jackson'
print(name[-1])             # n
print(name[-9])             # L
print(name[-8])             # <space>


# SLICING : You can cut the string using the indexes either through positive or through negative.

name = 'Micheal Jackson'
print(name[0:10])           # Micheal Ja
print(name[3:11])           # hael Jac
print(name[0:9999999])      # Micheal Jackson
print(name[0:0])            #
print(name[0:])             # Micheal Jackson
print(name[:])              # Micheal Jackson

# JUMPING VALUE

name = 'Micheal Jackson'
print(name[0:14:2])          # McaUcs
print(name[:14:3])           # Mhlas
print(name[::-1])            # nosakcal leahciM


# STRING FUNCTIONS/MEHTODS

name = 'Micheal Jackson'

print(type(name))                               # <class 'str'>
print(len(name))                                # 15

print(name.upper())                             # MICHEAL JACKSON
print(name.lower())                             # micheal jackson

print(name.capitalize())                        # Micheal jackson
print(name.split())                             # ['Micheal', 'Jackson']
print(name.replace('Jackson', 'Samuel'))        # Micheal Samuel

print(name.isupper())                           # False
print(name.islower())                           # False
print(name.isalnum())                           # False
print(name.isdecimal())
print(name.isdigit())
print(name.isnumeric())
