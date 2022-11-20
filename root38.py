# list comprehensions

multiples = []
for x in range(1, 11):
    multiples.append(x*7)

print(multiples)

# below in list comprehension, where the above code can be converted into 1 line of code
multiples_new = [x*7 for x in range(1, 11)]
print(multiples_new)

# example
languages = ["python", "perl", "ruby", "go", "java", "C"]
lengths = [len(language) for language in languages]
print(lengths)


# example (here we have iterated through a list with an if condition)
z = [x for x in range(1, 101) if x % 3 == 0]
print(z)
