import random
from venv import create

list_1  = [random.randint(0,100) for _ in range(1,100)]
list_2  = [random.randint(1,10) for _ in range(1,10)]


even= lambda x:True if x%2==0 else False
odd = lambda x:True if x%2!=0 else False
filter_even = list(filter(even,list_1))
filter_odd = list(filter(odd, list_2))
cube  = lambda x: x**3
square  = lambda x : x**2
product  = lambda x,y : x*y
square_cube = lambda x:square(cube(x))

print(filter_even)
print(filter_odd)
print("Cubes -->",[cube(i) for i in list_1])
print("Squares -->", [square(x) for x in list_1])
print("Squares Cubes -->",[square_cube(x) for x in list_1])
print("Product of lists -->",[product(x,y) for x,y in zip(list_1, list_2)])


#2 Create a dictionary of friends with three keys {“name”,”age”,”city”}. Create a lambda
# function on a dictionary with the key age. Use this function with sorted() to sort the
# dictionary by age

# dict = {"name":{"Anshul", "Gaurav","Rakesh"}, "age":{34,46,27}, "city":{"Kolkata", "Mumbai", "Delhi"}}
dict = [
    {"name":"Anshul", "age": 44, "city" : "Jaipur"},
    {"name": "Rakesh", "age": 23, "city" : "Pune"},
    {"name": "Gaurav", "age": 56, "city" : "Mumbai"}]


# print(dict.keys())
sorting_dict = lambda x : x["age"]
#
dict_sorted = sorted(dict, key=sorting_dict)

print(dict_sorted)

#3 Define a function apply_operation(a,b,operation) where operation is a lambda function.
#Inside apply_operation, call the operation(a,b) and return the output. Define the lambda
#functions sum, quotient, product (from Ex 1a) and difference for the two lists list_1, list_2
#similar to ex. 1 and print the output.


def apply_operation(a,b,operation):
    return operation(a,b)

sum = lambda x,y : x+y
quotient = lambda x,y : x//y
product = lambda x,y : x*y


print( apply_operation(4,5, sum))
print([apply_operation(x,y, product) for x,y in zip(list_1,list_2)])

#4 Create a function create_exponent that takes n as a parameter and returns a lambda
# function that is x raised to the power n.

def create_exponent(n):
    return lambda x: x**n

create_4th_exponent = create_exponent(4)
create_5th_exponent= create_exponent(5)

print([create_4th_exponent(x) for x in list_2])
print([create_5th_exponent(x) for x in list_2])


#5
reverse_string = lambda x: x[::-1]

dict_1 = {"hello":"olleh", "naman":"naman", "Python":"java", "dalad":"dalad"}

for key,value in (dict_1.items()):
    if (reverse_string(key)==value):
        print(key, True)
    else:
        print(key, False)

