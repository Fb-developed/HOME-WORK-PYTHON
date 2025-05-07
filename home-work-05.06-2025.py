# home=task

# salom = input("Введите тип животного: ")

# match salo :
#     case "cat" | "dog":
#         print("Млекопитающее")
#     case "bird":
#         print("Птица")
#     case "fish":
#         print("Рыба")
#     case _:
#         print("Неизвестный тип")

# task-0


# a = int(input())
# b = int(input())

# if a > b:
#     print(a)
# else :
#     print(b)

# task-1


# a = int(input())

# if a > 2000  and a < 2999:
#     print("NO")
# elif a  < 2000 and a > 1900:
#     print("YES")
# else :
#     print("Wrong Input")

# task-2


# a = int(input())
# b = int(input())

# if a == b or a != 1:
#     print("YES")
# else:
#     print("NO")

# task-3


# a = int(input())

# if a > 0:
#     print("1")
# elif a < 0:
#     print("-1")
# else:
#     print("0")

# task-4


# a = int(input())
# b = int(input())

# if a > b :
#     print("1")
# elif b > a :
#     print("2")
# else :
#     print("0")

# task-5


# a = int(input())
# b = int(input())
# c = int(input())

# if a > b and a > c:
#     print(a)
# elif b > a and b > c :
#     print(b)
# else:
#     print(c)

# task-6


# a = int(input())
# b = int(input())
# a1 = int(input())
# b1 = int(input())
# if a == a1 or b == b1 :
#     print("YES")
# else :
#     print("NO")

# task-7


# a = int(input())
# b = int(input())
# a1 = int(input())
# b1 = int(input())
# if (a - b) == (a1 - b1) :
#     print("YES")
# else:
#     print("NO")

# task-8


# a = int(input())
# b = int(input())
# a1 = int(input())
# b1 = int(input())
# if a == a1 or b == b1 or (a - b) == (a1 - b1) :
#     print("YES")
# else:
#     print("NO")

# task-9


# a = int(input())
# b = int(input())
# a1 = int(input())
# b1 = int(input())
# if (a - b) <= 1 and (a1 - b1) <= 1 :
#     print("YES")
# else:
#     print("NO")

# task-9


# a = int(input())
# b = int(input())
# a1 = int(input())
# b1 = int(input())
# if (a - b) == 2 and (a1 - b1) == 1 or (a - b) == 1 and (a1 - b1) == 2:
#     print("YES")
# else:
#     print("NO")

# task-10


# a = int(input())
# b = int(input())
# c = int(input())
# if (c % a == 0 and c < a * b) or (c % b == 0 and c < a * b) :
#     print("YES")
# else:
#     print("NO")

# task-11


# a = int(input())

# if a %  4 == 0 and a // 4 + 1 > 1:
#     print ("YES")
# else:
#     print("NO")

# task-12


# a = int(input())
# b = int(input())

# if a == 0 and b == 0:
#     print("INF")
# elif a == 0:
#     print("NO")
# else:
#     print(-b // a)

# task-13

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a == 0 and b == 0 :
#     print("INF")
# elif a == 0 or (c * (-b // a) +d == 0):
#     print("NO")
# else:
#     print(-b // a)

# task-14


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# res = a * 100 + b
# res1 = b * 100 + d
# res2 = res1 - res

# print(f"{res2 // 100} {res2 % 100}")

# task-15


# a = int(input())

# if a == 1 or a == 2 or a == 4 or a == 7 :
#     print("NO")
# else:
#     print("YES")

# task-16


# a = int(input())
# b = int(input())
# c = int(input())

# if c % a == 0:
#     res = c // a
# else :
#     res = c // a + 1
# res1 = res * 2 * b
# print(res1)

# task-17


# a = int(input())

# if a == 1 :
#     print("1 korova")
# elif a == 2:
#     print("2 korvy")
# else:
#     print( f"{a} korov")

# task-18


# a=int (input())
# match a:
#     case 3:
#         print('треугольник')
#     case 4:
#         print('квадрат, прямоугольник, ромб')
#     case 5:
#         print('пятиугольник')
#     case 7:
#         print('неизвестная фигура')

# task - 19


# status = input("Введите статус заказа:")
# match status:
#     case "new":
#         print("заказ создан") 
#     case "processing":
#         print('заказ в обработке')
#     case "shipped":
#         print('заказ отправлен')
#     case "delivered":
#         print("заказ доставлен")
#     case _:
#         print("неверный статус")

# task-20