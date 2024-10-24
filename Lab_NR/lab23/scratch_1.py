# A. Create a list of numbers from 1 to 10. Create a list squares_list using comprehension
# for the squares of the numbers (squares_list) . Create a generator expression for the
# same (squares_gen) . Print squares_list and squares_gen and observe the difference.
# Iterate over both and print the values.
# B. Repeat the above for a list/generator expression of even numbers
import random
from time import process_time

from Coursework_shyam.lab_lambdafunct import filter_even

number = [i for i in range(1,11)]
print(number)


print("Printing square_list")
square_list = [i**2 for i in number]
print(square_list)
for x in square_list:
    print(x)

square_gen = (i**2 for i in number)
print("\nPrinting square_gen")
print(square_gen)
for i in square_gen:
    print(i)


# get even number from number list
even_num = [2,4,6,8]
