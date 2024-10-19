'''Write a function to find the sum of squares of first N numbers
Write a function to convert the decimal number D into binary.
Write a function that computes the number of 1s in a binary representation of a decimal number, N.
Write a function to convert the binary number B into decimal.
Write a function that computes power - raise base to the n-th power. Eg. power(2, 5). Here base is 2 and n-th power is 5.
Write a function to check if a given number, N, is prime or not
Write a function to print individual digits of a number, N.
Write a function to print the first half of a string, S.
Write print alternate characters of a string, S
Write a program to concatenate two strings, S1 and S2.
Write a function to find the first occurrence of a character, c, in a string S.
Write a function to find the  highest frequency character in a string, S.
Write a function to replace all occurrences of a character, c,  with another character, d.
Write a function to trim leading whitespace characters from a string, S.
Write a function to count the number of occurrences of a word, W, in a sentence, S.
Write a function to check if two strings are anagrams of each other . Eg. listen and silent are anagrams, gram and arm are not anagrams
'''
from asyncio import ensure_future

from Coursework_shyam.lec26 import middle


#Write a function to find the sum of squares of first N numbers

# def sum_square(num):
#     z = int()
#     while num != 0 :
#         y = num**2
#         num = num - 1
#         z = z + y
#     return z
#
#
# def main():
#     num = 5
#     x = sum_square(num)
#     print(x)
#
# if __name__=="__main__":
#     main()


#Write a function to convert the decimal number D into binary
# Conversion steps:
#
#     Divide the number by 2.
#     Get the integer quotient for the next iteration.
#     Get the remainder for the binary digit.
#     Repeat the steps until the quotient is equal to 0.
# def cnvrt_dec_binary():
#     while num % 2 != 0:
#         y = num % 2
#

# Write a function that computes power - raise base to the n-th power. Eg. power(2, 5). Here base is 2 and n-th power is 5.
def power_calc(base, power):
    result = base**power
    return result

# Write a function to check if a given number, N, is prime or not
def check_prime(n):
    while n != 0:
        n = n-1
        if n/ n-1 ==0:
            print("This is a prime number")
        else:
            print("This is not a prime number")

#Write a function to print individual digits of a number, N.
def write_digits(num):
    num =list(str(num))
    for i in range(len(num)):
        prompt=print(num[i], end='')
    return prompt

write_digits(123)

# def main():
#     res = power_calc(2,5)
#     print(res)
#
# if __name__=="__main__":
#     main()
