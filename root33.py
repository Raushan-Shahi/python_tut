# string formatting
#the expression {:>3.2f} would align the text three spaces to the right,
#  as well as specify a float number with two decimal places.


name = "Raushan"
number = len(name) *3
print("Hello {}, your lucky number is {}.".format(name, number))
#In this statement we added a number to the string, thus formatting is a very powerful tool.

print("Hello, your lucky number is {number}, {name}.".format(name=name, number=3*len(name)))

price = 7.5
with_tax = price *1.09
print(price, with_tax)

print("Base price: Rs.{:.2f}. With Tax: Rs.{:.2f}".format(price,with_tax))