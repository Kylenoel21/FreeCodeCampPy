
#except = excluding errors, if u name drop a specified error to excuse, then it will only excuse
#that one type of error
#else = will happen if no errors occur
#Finally = will occur no matter if there is an error or not, it is absolute!



class JustNotCoolError(Exception):
    pass

x = 2
try:
    raise JustNotCoolError("This just isnt cool man")
    #raise Exception("I'm a custom exception!")
   # print(x / 0)
   #  if not type(x) is str:
   #      raise TypeError("Only strings are allowed.")

except NameError:
    print('NameError means something is probably undefined.')

except ZeroDivisionError:
    print('Please do not divide by Zero.')

except Exception as error:
    print(error)

else:
    print('No errors!')

finally:
    print("I'm going to print with or without an error.")
