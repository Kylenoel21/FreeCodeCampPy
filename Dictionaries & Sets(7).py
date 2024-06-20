                            #Dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))


                            #Access items in a dictionary
print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())

#list all values
print(band.values())

#list of key/value pairs as tuples
print(band.items())

#verify if key exists
print("guitar" in band)
print("triangle" in band)

                            #Change values
band["vocals"] = "Coverdale"
band.update({"bass":"JPJ"})

print(band)

                        #Remove items
print(band.pop("bass"))         #bass and jpj have been removed, pop only returns the value
print(band)

band["drums"] = ("Bonham")
print(band)

print(band.popitem())       #Removes the last key value, that was added to the dictionary
print(band)

                    #Delete and clear itemms
band["drums"] = ("Bonham")
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2


                                    #Copy dictionaries
# band2 = band           #creates a reference (both refereing to same place in memory or dictionary)
# print("Bad copy!")
# print(band2)
# print(band)
#                               #This is what NOT to do when making copies
# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

                    #Or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)

                        #Nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
 }
member2 = {
    "name": "Page",
    "instrument": "guitar"
 }
band = {                        #band is nesting these dictionaries
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

                    #Sets

nums = {1, 2, 3, 4}

nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums2))
print(len(nums))                #There are 4 elemnts in our set

                    #No duplicates allowed!
nums = {1, 2, 2, 3}
print(nums)

#True is a dupe of 1, False is a dupe of zero. Dupe = Duplicate
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

#1 came before True, so it ignored true. False came before 0, so it ignored 0. However false has same value as 0, so it comes before rest in the set

#check if a value is in a set
print(2 in nums)

#but u cannot refer to an element in the set with an index position or a key like dictionary


            #Add a new element to a set
nums.add(8)
print(nums)

            #Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)         #You can use update with lists, tuples, and dictionaries too
                    #Instead of nums update u can use list update or tuples update and it'll still work


            #Merge 2 sets to create a new setr
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)       #Union allows u to merge 2 different sets
print(mynewset)

        #Keep only the duplicates
one = {1, 2, 3}
two = {2, 3,4}

one.intersection_update(two)
print(one)

            #Keep everything except duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)              #Symmetric difference gets rid of all duplicates, intersection keeps all duplicates

# one.