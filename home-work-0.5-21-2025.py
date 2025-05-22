# def outer():
#     pred = 'None'
#     def inner(n):
#         nonlocal pred
#         result = f"Predushi znacheni {pred} novoe {n}"
#         pred = n
#         return result
#     return inner
# obj1 = outer()
# print(obj1(10))
# print(obj1(20))

# task-1





# def outer(n):
#     cnt = 0
#     def inner():
#         nonlocal cnt
#         if cnt < n:
#             cnt+=1
#             return 'vizov vpolnen'
#         else:
#             return 'limit isprechen'
#     return inner
# obj1 = outer(2)
# print(obj1())
# print(obj1())
# print(obj1())

# task-2




# def outer():
#     res = []
#     def inner(n):
#         res.append(n)
#         return res
#     return inner
# add= outer()
# print(add(10))
# print(add(20))

# task-3




# def outer():
#     n = 0
#     def inner():
#         nonlocal n
#         n+=1
#         return n, 'cekund proshlo'
#     return inner
# obj1 = outer()
# print(obj1())
# print(obj1())

# task-4




# def outer(n):
#     def inner(a):
#         return a * n
#     return inner
# obj1 = outer(5)
# print(obj1('SALOM '))

# task-5




# def outer(n):
#     def inner(a):
#         return len(a) > n
#     return inner
# obj1 = outer(5)
# print(obj1('Salomd'))

# task-6




# def outer(n):
#     def inner(a):
#         return a * (1 - n / 100)
#     return inner
# obj1 = outer(10)
# print(obj1(200))

# task-7




# def outer(n):
#     def inner():
#         return f"welcome {n}"
#     return inner
# name = outer('ali')
# print(name())

# task-8




# def outer(pas):
#     def inner():
#         return f"user_{pas}_2025"
#     return inner
# password1 = outer('secure')
# print(password1())

# task-9