'''1- Reverse a string without using a third variable (using two pointers)'''
# def reverse(st):
#     a = list(st)
#     left = 0
#     right = len(st) - 1
#     while left < right:
#         a[left],a[right] = a[right],a[left]
#         left += 1
#         right -= 1
#     return ''.join(a)
# st = 'Hello World'
# print(reverse(st))
'''2- Reverse of a string - Using a loop'''
# str = input("Enter the string")
# n = len(str)-1
# for i in range(n,-1,-1):
#     print(str[i],end="")
'''Reverse of a string - Using Recursion'''
# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]
# s = "Saurav Kumar"
# print(reverse(s))
'''Reverse of a string - Using Slice'''
# str = "Saurav Kumar"
# print(str[::-1])
'''3- Reverse a sentence program same Reverse words in string '''
# str = "Hello world this is an example"
# words = str.split()
# words = words[::-1]
# rev = ' '.join(words)
# print(rev)
'''4- Find vowel in your name.'''
# def vowels(str):
#     v = "aeiouAEIOU"
#     f = [i for i in str if i in v]
#     return f
# input = "saurav"
# print(vowels(input))
'''5- Write code for counting different characters in string'''
# str = "saurav"
# count = {}
# for i in str:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
# print(count)
'''6- Count the number of occurrence of a character in string'''
# str = 'saurav kumar'
# char = 'a'
# count = 0
# for i in str:
#   if i == char:
#     count += 1
# print(count)

#initializing a string
str = "Banana"
print(str.count('a'))

'''7- Find the world in the given sentence.'''
# str = "the world in the given sentence."
# print('world' in str)
