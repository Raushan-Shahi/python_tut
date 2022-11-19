#multiplication table


def multiplication_table(start, stop):
	for x in range(1,stop+1):
		for y in range(1,11):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above