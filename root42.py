#dictionaries
# they are mutable  



file_count= {"jpg":10, "txt":14, "csv":32, "py":43}
print(file_count)
print(file_count["txt"])
print("jpg" in file_count)
print(type(file_count))
file_count["cfg"] = 9
file_count["csv"] = 34  # this will replace the previous key of the dictionary 

for extension in file_count:
    print(extension)

#we can use .items for iterating through both keys and values
# we can use .keys to accesss the keys
# We can use .value to access the value 

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for keys,values in cool_beasts.items():
    print("{} have {}".format(keys,values))