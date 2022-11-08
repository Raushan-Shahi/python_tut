#if statement 
#length of string comparison 



name = input("enter your name: ")
length = len(name)

if length < 2:
    print("Name must be at least 3 characters")
elif length > 50:
    print("name can be maximum 50 characcters")
else:
    print("the name looks good")
