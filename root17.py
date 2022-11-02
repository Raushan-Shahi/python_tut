# project weight converter

print("Welcone to weight calculator")
weight = int(input("Enter your weight: " ))
unit = input("enter your unit:(l)lbs or (k)kgor (g)grams" ) 
convert = input("The unit you want " )

if unit == "l" and convert == "k":
    print(f'{weight*4.5} {convet}')

elif unit == "k" and convert == "l":
    print(f'{weight/4.5} {convert}')
elif unit == "k" and convert == "g":
    print(f'{weight*1000} {convert}')
elif unit =="g" and convert == "k":
    print(f'{weight/1000} {convert}')
elif unit == "g" and convert == "l":
    print(f'{weight/4500} {convert}')
else:
    print(f'{weight*4500} {convert}')





