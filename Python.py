'''1- Simple pyramid pattern'''
n=4
for i in range(n):
    print("*" * (i+1))
'''2- Diamond Shaped Pattern'''
# def pyramid_pattern(n):
#   for i in range(n):
#     print(" "*(n-i-1)+"*"*(2*i+1))
#   for i in range(n-2,-1,-1):
#     print(" "*(n-i-1)+"*"*(2*i+1))    
# pyramid_pattern(5)
'''Print the following start pattern'''
n = 3
for i in range(3):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
'''3- Write code for multiplying and diving a number with 2 without using arithmetic operator using bitwise operators'''
# def multiply2(n):
#     return n << 1
# def divide2(n):
#     return n >> 1
# n = 10
# print(multiply2(n))
# print(divide2(n))
'''4- Write a code to swap variable without using the third variable'''
# def swap(a, b):
#     a = a ^ b
#     b = a ^ b
#     a = a ^ b
#     return a, b
# a = 5
# b = 10
# print(a,b)
'''5- Prime number '''
# num = int(input("Enter a number: "))
# if num == 1:
#   print('Not prime number')
# if num > 1:
#    for i in range(2,num):
#        if (num % i) == 0:
#            print("not a prime number")
#            break
#    else:
#        print(num,"prime number")
'''6- Fibonacci series using recursion '''
# def Fibonacci(n):
#     if n < 0:
#         print("Enter the Positive Number")
#     elif n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1)+ Fibonacci(n-2)
# n = int(input('Enter the number: '))
# for i in range(n):
#     print(Fibonacci(i))
'''2nd Apporch'''
# a = 0
# b = 1
# num = int(input("Enter the number: "))
# if num == 1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(2,num):
#         c = a + b
#         a = b
#         b = c
#         print(c)
'''7- A number is Palindrome'''
# a = input("Enter a word: ")
# rev = a[ ::-1]
# if a == rev:
#     print('It is palindrome')
# else:
#     print('It is not Palindrome')
'''2nd Apporch using casefold'''
# a = input("Enter a word: ")
# my_str = a.casefold()
# rev = reversed(a)

# if list(a) == list(rev):
#    print("Palindrome.")
# else:
#    print("Not Palindrome.")
'''8- Armstrong Number'''
# num = int(input('Enter a number:' ))
# sum = 0
# temp = num
# while temp > 0:
#   digit = temp%10
#   sum += digit ** 3
#   temp //= 10
# if num == sum:
#   print('Armstrong number')
# else:
#   print('Not Armstrong number')
'''9- Find square root of a number **'''
# num = int(input("Enter the number: "))
# sr = num**0.5
# print(sr)
'''2nd apporch'''
# import math
# num = int(input("Enter the number: "))
# sr = math.sqrt(num)
# print(sr)
'''10- Reverse of a number '''
# n = 12345
# rev = 0
# while(n > 0): 
# 	digit = n % 10
# 	rev = rev*10 + digit 
# 	n = n // 10
# print(rev) 
'''2nd Apporch'''
# a = input("Enter a number: ")
# rev = a[ ::-1]
# print(rev)
'''Factorial'''
# num = int(input("Enter a number: "))
# fact = 1
# if num < 0:
#     print("Factorial of 0 is not exist")
# if num == 0:
#     print("Factorial of 0 is",1)
# if num > 0:
#     for i in range(1,num+1):
#         fact = fact*i
# print(fact)
'''2nd Apporch'''
# def fact(n):
#     if n == 1 or n == 0:
#         return 1
#     return n *fact(n-1)
# f =fact(4)
# print(f)