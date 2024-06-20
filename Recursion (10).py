                                     # Recursions
#Recursions happen when a function calls itself

def add_one(num):

    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)           #Return makes it so the value is recursive, failure to do so
                                    #Will result in the answer being 'None'
mynewtotal = add_one(0)             #None isnt True or False, it simply just is
print(mynewtotal)






                                    #Example.py
value = "y"
count = 0
                                    # while value: same as   -->   while value == True
while value:
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = 0
        continue


