# Lamda function (anonymous function) is a single expression that returns a value
#Lamdas are often used inside another function, when you need a quick funtion that u dont wanna save it for later



squared = lambda num : num * num

print(squared(2))
                                        #OR
# def squared(num): return num * num
#
# print(squared(2))



addTwo = lambda num : num + 2

print(addTwo(12))
                                        #OR
# def addTwo(num): return num + 2
#
# print(addTwo(12))



#function expression
sum_total = lambda a, b : a + b

print(sum_total(10, 8))

# def sum(a, b): return a + b
#
# print(sum(10, 8))




def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))



                                    #Map

numbers = [3,7,12,18,20,21]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))



                                    #Filter


odd_nums = filter(lambda num : num % 2 !=0, numbers)
#
print(list(odd_nums))




                        #Reduce  (can be complex, but when simple, it just adds everything)
#acc ---> accumalator or subtotal                   curr ---> current item


from functools import reduce



numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)
#reduce dont use if there is easier solution like below
print(sum(numbers, 10))






names = 'Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt'

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)


#Higher order functions  ---> If it recieves a function as an argument, or if it returns a function