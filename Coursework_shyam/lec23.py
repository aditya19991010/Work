# 1. convert farenheit to celcius

def Faren_to_celc(F):
    c =  ( F - 32 ) * ( 5/9)
    return (c)

def main():
    F = input("Enter a value:\n")
    c = Faren_to_celc(F)
    print(f"The value after conversion in {c}")

if __name__ == '__main__':
    main()

# 2. check if the number is even or odd

# num = input()
# def check_odd_even():
#     if num % 2 == 0 :
#         print("This is an even number")
#     elif num == 0 :
#         print("please enter the naturak nu")

# 3. check if a given strinfg is palindrome or note
#4. print 10 terms of fibonacci series
