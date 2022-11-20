#iterating over lists and tuples

animals = ["lion", "Zebra", "dolphin", "monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

winners = ["ashley", "dylan", "reese"]
for index,person in enumerate(winners):
    print("{}  -  {}".format(index+1, person))


def full_emails(people):
    result =[]
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

result = full_emails([("raushan@gmail.com","Raushan Shahi"), ("xyz@gmail.com","xyz"),("Niharika@gmail.com","Niharika verma")])
print(result[0])
print(result[1])
print(result[2])



def skip_elements(elements):
	result =[]
	for index,elem in enumerate(elements):
		if index%2 ==0:
			result.append(elem)
	
	return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']