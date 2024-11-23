# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# # while loop
# number = 1
# while number <= 5:
#     print(number)
#     number = number + 1
    
# # For loop

# names = ['John', 'Jane', 'Mike', 'Mary']

# for name in names:
#     print(name)
    
# for name in enumerate(names):
#     print(name)
    
# for index, name in enumerate(names):
#     print(f'{index+1}, {name}')
    
# # List all numbers between 10 and 100 and state whether they are odd or even

# for num in range (10, 100):
#     # if num % 2 == 0:
#     #     print(f'{num} is even')
#     # else:
#     #     print(f'{num} is odd')
#     print(f'{num} is {'even' if num % 2 == 0 else 'odd'}')
    
# # for else

# for i in range(10):
#     print(i)
#     if i == 6:
#         break
# else:
#     print('loop finished')
    
# Output if a number is prime
# Number is prime if it is divisible only by 1 and itself

number = 17
for i in range (2, number):
    if number % i == 0:
        print('Number is not prime')
        break
else:
    print('Number is prime')