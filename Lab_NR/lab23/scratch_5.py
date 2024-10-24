#fibbonacci
from Coursework_shyam.lec26 import bottles


# Write a generator function fibonacci that yields the Finocacci series number infinitely.
# Create a generator expression fib_gen that calls this function. Print the 10 numbers of
# this generator expression using next()
# B. Repeat the same for generating even_numbers
#
# C. Repeat the same for generating expressions for powers of 2

def fibbonacci():
    a=0
    b = 1
    while True:
        yield a
        a =b
        b = a+b
    return b

fib_gen = (num for num in fibbonacci())

# Print the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))
