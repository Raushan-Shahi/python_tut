# This is a code to calculate your age in the ongoing year 



#  birth_year = input('Birth year: ')
#  age = 2022- birth_year
#  print(age)

# the above code won't work as this code is subtracting string from int

current_year = input('current year: ')
birth_year = input('Birth year: ')
print(type(birth_year))
age = int(current_year)- int(birth_year)
print(type(age))

print(age)