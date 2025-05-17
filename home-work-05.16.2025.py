# n = input()
# def ispalidrom(n):
#     org_words = n[: :-1]
#     if n == org_words:
#         return('palidrom')
#     else:
#         return('no palidrom')

# print(ispalidrom(n))

# task-1



# def sum(lst):
#     sum = 0
#     for i in lst:
#         sum += i
#     return sum
# print(sum([1, 2, 3, 4, 5]))

# task-2



# name = input()
# def greet(name='Guest'):
#     print(f'Hello {name}')
# greet(name)

# task-3



# fib1 = int(input())
# def fib(fib1):
#     a = 0
#     b = 1
#     if fib1 == 0:
#         return a
#     elif fib1 == 1:
#         return b
#     else:
#         for i in range(2, fib1 + 1):
#             c = a + b
#             a = b
#             b = c
#         return b
# print(fib(fib1))

# task-4




# str = input()
# def count_vowels(str):
#     vowels = 'aeiouAEIOU'
#     count = 0
#     for char in str:
#         if char in vowels:
#             count += 1
#     return count
# print(count_vowels(str))

# task-5




# lst = [1, 2, 3, 3, 2, 4, 5]
# def remove_duplicates(lst):
#     res = []
#     for i in lst:
#         if i not in res:
#             res.append(i)
#     return res
# print(remove_duplicates(lst))

# task-6



# lst = [1, 2, 3, 4, 5]
# def get_even_numbers(lst):
#     even = []
#     for i in lst:
#         if i % 2 == 0:
#             even.append(i)
#     return even
# print(get_even_numbers(lst))

# task-7




# n = int(input())
# def sum_of_digits(n):
#     sum = 0
#     while n > 0:
#         digit = n % 10
#         sum += digit
#         n //= 10
#     return sum
# print(sum_of_digits(n))

# task-8



# def find_first_capital(words):
#     word = words.split()
#     for i in word:
#         if i and i[0].isupper():
#             return i
# print(find_first_capital('hello World'))

# task-9



# def max_of_three(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > c and b > a:
#         return b
#     else:
#         return c
# print(max_of_three(1, 2, 3))

# task-10