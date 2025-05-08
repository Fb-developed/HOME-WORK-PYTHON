

        # while

# n = int(input())
# while n > 0 :
#     print(n % 2, end='')
#     n//=2

# task-1




        # while

# n =int(input())
# i = 1
# while i < n + 1 :
#     if n % i == 0:
#         print(i,end=' ')
#     i+=1

        # for

# n = int(input())
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i, end=' ')

# task-2




        # while

# n = int(input())
# i = 1
# while i < n :
#     if n % i == 0 and i > 1:
#         print(i)
#         break
#     i+=1

        # for

# n = int(input())
# for i in range(1, n):
#     if n % i == 0 and i > 1:
#         print(i)
#         break

#task-3




        # while

# n = int(input())
# i = 1
# while i < n:
#     if i ** 2 < 50:
#         print(i**2, end=' ')
#     i+=1 

        # for

# n = int(input())
# for i in range(1, n):
#     if i ** 2 < 50:
#         print(i ** 2, end=' ')

# task-4




        # while

# n = int(input())
# i = 1
# while i <= n:
#     if i == n:
#         print("YES")
#         break
#     i*=2 
# else:
#     print("NO")

        # for
# task-5





        # while

# n = int(input())
# i = 1
# while i <= n :
#         if i <= n:
#                 print(i, end=' ')
#         i*=2

# task-6




        # while

# a = int(input())
# b = int(input())
# if a > b:
#         a, b = b, a
# cnt = 0
# while a <= b:
#         cnt+=1
#         a+=1
# print(cnt)

        # for

# a = int(input())
# b = int(input())
# if a > b:
#         a, b = b, a
# cnt = 0
# for i in range(a-1, b):
#         cnt+=1
# print(cnt) 

# task-7




        # while

# a = int(input())
# b = int(input())
# if a > b:
#         a, b = b, a
# sum = 0
# while a <= b:
#         sum+=a
#         a+=1
# print(sum)

        # for
# a = int(input())
# b = int(input())
# if a > b:
#         a, b = b, a
# sum = 0
# for i in range(a, b+1):
#         sum+=i
# print(sum) 

# task-8




        # while

# n = int(input())

# cnt = 0
# i = 1
# while i <= n:
#         org = i
#         rev = 0
#         while org > 0:
#                 rev = rev * 10 + org % 10
#                 org//=10
#         if rev == i:
#                 cnt+=1
#         i+=1
# print(cnt)

        # for
# n = int(input())
# cnt = 0
# rev = 0
# for i in range(1, n + 1):
#         org = i
#         rev =  0
#         for  j in range(1, i):
#                 rev = rev * 10 + i % 10
#                 org//=10

#         if rev == i:
#                 cnt+=1
# print(cnt)

# task-9