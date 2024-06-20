            # Functions are re-useable parts of code
def hello_world():
    print("Hello world!")

hello_world()                         # Functions need to be all lower case!
                                    # Only use _ to seperate words, no Capital letters, or hyphens


#       print(num1 + num2)              # Parameters never change, however arguments can

# sum(2,3)
# sum(1,7)
# sum(100,3)




def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2
                            #give num1 and num2 values of 0 so code doesn't crash
                           #Make sure they are integers and then apply "if" value to return if the
                            #criteria isnt met
total = sum(7, 2)
print(total)





def multiple_items(*args):              #* = multiply, and args is short for arguments
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sara")


def mult_named_items(**kwargs):          #kwargs = Key Word Arguments
    print(kwargs)
    print(type(kwargs))


mult_named_items(first = "Dave", last = "Gray")