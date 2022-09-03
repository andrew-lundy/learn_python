# Exercise: https://www.learnpython.org/en/Generators
# Write a generator function which returns the Fibonacci series. They are calculated using the following formula: The first two numbers of the series is always equal to 1, and each consecutive number returned is the sum of the last two numbers. Hint: Can you use only two variables in the generator function? Remember that assignments can be done simultaneously.

import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

# for random_number in lottery():
    #    print("And the next number is... %d!" %(random_number))

# def fib():
#     a, b = 1, 1
#     while 1:
#         yield a
#         a, b = b, a + b

# for number in fib():
#     print(number)

def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci(10)))