import math
# String data type

#literal assignment
first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))



#contructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))



# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)



# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)



# Multiple lines
multiline = '''
Hey, how are you?

I was just checking in
                                    All good?

'''
print(multiline)



# Escaping special charatcters
#\t = tab (space). \n = new line. \' counts as apostrophes. \\ = or

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)



# String Methods
print(first)
print(first.lower())            # Makes whole word lower case
print(first.upper())            # Makes whole word Upper case
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                          "
multiline = "                                " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")



# Build a menu
title = "menu".upper()
print(title.center(20, "="))
#20 is how much of the thing you want. center puts it in the center. and = says you want = 20 times
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$3".rjust(4))
print("Cheesecake".ljust(16, ".") + "$9".rjust(4))

print("")



#string index values
print(first[1])         #1 is 2nd value in name, bcuz index starts at 0
print(first[-1])         # if you want the first value then type zero
print(first[1:-1])        #-1 helps you find the last value, useful if you NEED to get the last value right
print(first[1:])         #without specifying, this shows you rest of charcters in the word



# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))



#Boolean data type
myvalue = True           #Gotta be Capital letter
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3j           #for Electrical engineering
print(type(comp_value))
print(comp_value.real)          #real = real number value
print(comp_value.imag)        #imag = imaginary number value


# Built in finctions for nummbers

print(abs(gpa))           #abs = absolutle value
print(abs(gpa * -1))

print (round(gpa))         #rounds to the nearest integer

print (round(gpa , 1))    #rounds to the



#math

print(math.pi)
print(math.sqrt(64))       #sqrt = square root
print(math.ceil(gpa))
print(math.floor(gpa))



#Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))



# Error if you attempt to cast incorrect data
zip_value = int("New York")