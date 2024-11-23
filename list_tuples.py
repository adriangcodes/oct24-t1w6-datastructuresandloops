# List - Array - ordered collection of values - mutable - indexed
numbers = [13, 2, 23, 53] # creates new  list, assigns it the variable numbers
print(numbers)
print(numbers[-1])

numbers[2] = 17
print(numbers)

# numbers[5] = 72
numbers.append(13) # can only append a single value at a time
print(numbers)

numbers.insert(3, 99)
print(numbers)

# numbers.pop() # leave blank to remove the last item
# print(numbers)

popped_value = numbers.pop(2)
print(numbers)
print(popped_value)

# numbers.remove(13) # removes the first instance of 13
# print(numbers)

numbers.sort(reverse=True)
print(numbers)

print(numbers.count(13))
print(numbers.count(1234))

# Tuple - ordered collection of values - zero indexed - immutable

names = ("John", "Jane", "Mike", "Mary")
print(names)
print(type(names))

# print(names[1])
# names[2] = "Somebody"

# print(names.index('Foo'))
print(len(names))