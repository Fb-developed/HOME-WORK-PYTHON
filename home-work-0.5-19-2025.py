# n = input()
# def palidrome(n):
#     str = n[::-1]
#     if  str == n:
#         print('True')
#     else:
#         print('False')

# palidrome(n)

# task-1


# def sum_list(lst):
#     sum = 0
#     for i in lst:
#         sum+=i
#     print(sum)

# sum_list([1,2,3,4,5])

# task-2



# def names(name='Guest'):
#         return(f"Hello {name}")

# print(names())  
# print(names('Ali'))

# task-3



# n = int(input())
# def fibonachi(n):
#     a = 0
#     b = 1
#     if n == 0:
#         return a
#     elif n == 1:
#         return b
#     for i in range(2, n+1):
#         c = a + b
#         a = b
#         b = c
#     return b

# print(fibonachi(n))

# task-4



# def sum_three(a, b, c):
#     if a > b and a > c:
#         print(a)
#     elif b > a and b > c:
#         print(b)
#     else:
#         print(c)

# sum_three(1,3,5)

# task-5


# n = input()
# def vowels(n):
#     vow = 'aieouyAIEOUUY'
#     cnt = 0
#     for  i in n:
#         if i in vow:
#             cnt+=1
#     print(cnt)
    
# vowels(n)

# task-6



# def remove_lst(lst):
#     lst1 = []
#     for i in lst:
#         if i not in lst1:
#             lst1.append(i)
#     return lst1

# print(remove_lst([1,1,23,4,5,4,2]))

# task-7



# def get_even(lst):
#     even = []
#     for i in lst:
#         if i % 2 == 0:
#             even.append(i)
#     return even

# print(get_even([1,1,23,4,5,4,2]))

# task-8



# n = int(input())
# def sum_of_digits(n):
#     sum = 0
#     while n  > 0:
#         digit = n % 10
#         sum += digit
#         n//=10
#     return sum

# print(sum_of_digits(n))

# task-9



# def capital(words):
#     word = words.split()
#     for i in word:
#         if i[0].isupper():
#             return i

# print(capital('hello, fello, Salom'))

# task-10