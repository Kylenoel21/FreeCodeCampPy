
users = ('Dave','John','Sara')               #lists are 1 of 4 collection data types

data = ['Dave', 42, True]
                                            #every list starts from 0
emptylist = []

my_tuple = (1, 2, 3)

my_list = list(my_tuple)
my_list.append(4)
my_tuple = tuple(my_list)
print(my_list)



print("Dave" in emptylist)        #tuples = once they're values are made, they cannot be modified like the order they're in etc.
                                #Attribute Error is raised when u try to call an attribute
print(users[0])                 # of an object that doesnt exist
print(users[-1])

print(users.index('Sara'))

print(users[0:2])

print(len(data))






# users.append('Elsa')              #(THESE DONT WORK SOMEHOW
# print(users)                      #I don't think its supported on this python version, cuz guy
                                    #uses sommething else
# users += ['Jason']
# print(users)

# users.extend(('Robert','Jimmy'))
# print(users)
#
# users.insert(0, 'Bob')
# print(users)

#users[2:2] = ['Eddie','Alex']     #saying where u want it to go

#users[1:3] = ['Robert', 'JPJ']      #replaces values

#users.remove('Bob')

# print(users.pop())            #copies last value at the end(Jimmy, Jimmy)

#del users[0]                  #0 is the 1st value

# del data
data.clear()
print(data)

#users[1:2] = ['dave']
# users.sort()
# print(users)

# users.sort(key=str.lower)    #key string lower case value
# print(users)                  #data types need to be same when sorting, eg. all strings



nums = [4,5,6,7,89,3,32]
#nums.reverse()                  #reverses the order of the nummbers
#print(nums)

# nums.sort(reverse=True)           #Reverses from biggest to smallest
# print(nums)                 #sorts them ascendingly, then reverses it descendingly




print(sorted(nums, reverse=True))
print(nums)



# Different ways to make a copy
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()                   #sorting them ascendingly
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)








#Tuples

mytuple = tuple(('Dave', 42,True))

anothertuple = (1,4,2,8,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(my_tuple)
newlist.append('Neil')
newtuple = tuple(newlist)       #original mytuple doesnt change but new tuple is being added to it
print(newtuple)                 #putting tuples together = "Packing tuples"

(one, *two, hey) = anothertuple
print(one)                     #*provides all values between the two values in brackets
print(two)
print(hey)

# print(data.)    =   shows u all the different types of data u have!
print(anothertuple.count(2))    #counts how many2 2's there are, which is 3