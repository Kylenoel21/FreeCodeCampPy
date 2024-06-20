import os
# R = READ
# A = APPEND  (Update)
# W = WRITE
# X = CREATE

# Read - error if it doesnt exist

# f --> file



f = open("names")
                  #(read, means read the file. read 4 means 1st 4 characters)
#print(f.read())
#print(f.read(4))



                 #(first print reads 1st line, 2nd priont auto reads 2nd line)
#print(f.readline())
#print(f.readline())


for line in f:
    print(line)

f.close()

      #Whenever u open a file, when ur finished with it, u need to close it


try:
    f = open("names")
    print(f.read())
except:
    print("The file you want to read doesnt exist")
finally:
    f.close()


                # Append - creates the file if it doesnt exist (gonna open the file anyway)
        # By default when you open its to read, so u dont have to put in "r", however with any other
        # command, u need to specify what ur gonna do with the file. "a" ----> Append

f = open("names", "a")
f.write("Neil\n")
f.close()

f = open("names")
print(f.read())
f.close()

# Write (overwrite)     w --> write
f = open("context", "w")
f.write("I deleted all of the context")
f.close()

f = open("context")
print(f.read())
f.close()


                            #  Two ways to create a new file

#  Opens a file for writing, creates a file if it doesnt exist
f = open("name_list", "w")
f.close()


                # CREATES THE SPECIFIED FILE, BUT RETURNS AN ERROR IF THE FILE EXISTS

if not os.path.exists("dave"):
    f = open("dave", "x")
    f.close
                            # X = Create


#  Delete a file
# Avoid an error if it doesnt exist
if os.path.exists("dave"):
    os.remove("dave")
else:
    print("The file you wish to delete doesnt exist")




with open("more_names") as f:
    content = f.read()

with open("names", "w") as f:
    f.write(content)

    # Your telling it to read "more_names", then write its content in "names".
    # Essentially copying and pasting