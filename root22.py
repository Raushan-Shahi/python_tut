#nested for loop 
# end=" " is used to print a break in line and print in new line 


for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) +"|" + str(right) + "]", end=" " )
    print()