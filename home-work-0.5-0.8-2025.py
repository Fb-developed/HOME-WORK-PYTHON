

        # for

# n = int(input())
# res = 1
# for i in range(n):
#         res*=2
# print(res)

    # while

# n = int(input())
# res = 1
# i = 1
# while i < n + 1:
#     res*=2
#     i+=1
# print(res)


# task-1



        # for

# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum+=i*i
# print(sum)

        # while

# n = int(input())

# sum = 0
# i = 1
# while i < n + 1 :
#     sum+=i*i
#     i+=1
# print(sum)


# task-2



        # for

# n = int(input())
# sum = 1
# for i in range(1, n + 1):
#     sum*=i
# print(sum)

        # while

# n = int(input())
# i = 1
# sum = 1
# while i < n + 1:
#     sum*=i
#     i+=1
# print(sum)


# task-3



        # for

# n = int(input())
# k = int(input())
# fac1=1
# fac2=1
# fac3=1
# for i in range(1, n + 1):
#             fac1*=i
# for i in range(1, k + 1):
#             fac2*=i
# for i in range(1, (n-k) + 1):
#             fac3*=i
# print(fac1//(fac2 * fac3))

        # while

# n = int(input())
# k = int(input())
# fac1=1
# fac2=1
# fac3=1
# i = 1
# while i <= n:
#         fac1*=i
#         i+=1
# while i <= n:
#         fac2*=i
#         i+=1
# while i <= (n - k):
#         fa3*=i
#         i+=1
# print(fac1 // (fac2 * fac3))


# task-4




        # for

# a = int(input())
# n = int(input())

# sum = 0
# for i in range(n + 1):
#     sum+=a**i
# print(sum)

    # while

# a = int(input())
# n = int(input())

# sum = 0
# i = 0
# while i <= n :
#     sum+= a ** i
#     i+=1
# print(sum)


# task-5



        # for

# n = int(input())
# sum = n
# for i in range(2):
#     sum+=1
# print(sum)

        # while

# n = int(input())
# sum = n
# i = 0
# while i < 2 :
#     sum+=1
#     i+=1
# print(sum)


# task-6



        # for

# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum+= 1 / i

# print(sum)

        # while

# n = int(input())
# sum = 0
# i = 1
# while i < n :
#     sum+=1 / i
#     i+=1
# print(sum)


# task - 7


        # for
# n = int(input())
# sum = 0
# fac = 1

# for i in range(1, n + 1):
#     fac*=i
#     sum+=1/fac
# print(sum + 1)


        # while
# n = int(input())
# sum = 1
# i = 1
# fac = 1
# while i < n:
#     fac*=i
#     sum += 1 / fac
#     i+=1
# print(sum)


# TASK-9


    # for
# n = int(input())
# a, b = 0, 1
# if n == 0:
#     print(a)
# else:
#     for i in range(2, n + 1):
#         a, b = b, a + b
#     print(b)

# task - 10


        # for

# n = int(input())
# b = True
# cnt=0
# f1=1
# f2=1
# for i in range(100):
#         f3=f1+f2
#         cnt+=1
#         if f1 > n:
#                 b=False
#                 break
#         if f1==n:
#                 break
#         f1=f2
#         f2=f3
#         if b==False:
#                 print(-1)
#         else :
#                 print(cnt)

                # while
# n = int(input())
# b = True
# cnt=0
# f1=1
# f2=1
# while True:
#         f3=f1+f2
#         cnt+=1
#         if f1 > n:
#                 b=False
#                 break
#         if f1==n:
#                 break
#         f1=f2
#         f2=f3
#         if b==False:
#                 print(-1)
#         else :
#                 print(cnt)