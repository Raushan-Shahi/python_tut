def count_lettes(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


print(count_lettes("aaa"))
print(count_lettes("aaabvcfbds  "))