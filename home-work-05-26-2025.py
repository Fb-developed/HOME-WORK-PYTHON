import random



# for i in range(10):
#     t = random.randrange(0,20,2)
#     print(t)

# task-1



# cnt = 0
# for i in range(100):
#     t = random.random()
#     if t > 0.3 and t < 0.7:
#         cnt+=1
# print(cnt)

# task-2



# lst = ['ali', 'zarina', 'bobur', 'dilshod', 'sardor', 'vali', 'nazar','shahrom','madina','sardorbek']
# print(random.sample(lst,3))

# task-3



# lst = ['banana', 'apple', 'orange', 'kiwi','lemon']
# for i in range(3):
#     random.shuffle(lst)
#     print(lst)

# task-4


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random.shuffle(lst)
# print(random.sample(lst,3))

# task-5


# lst = []
# for i in range(7):
#     t = random.randrange(1,99,2)
#     lst.append(t)
# sor = sorted(lst)
# sor.reverse()
# print(sor)

# task-6



# sum = 0
# for i in range(10):
#    t = random.randint(1,5)
#    sum += t
# print(sum/10)

# task-7




# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# lst1 = []
# for i in range(5):
#     t = random.choice(lst)
#     lst1.append(t)
# print(lst1)

# sum = 0
# for i in lst1:
#     sum += i
# print(sum)

# task-8



# lst = ['red','green', 'blue']
# cnt1 = 0
# cnt2 = 0
# cnt3 = 0
# for i in range(100):
#     t = random.choices(lst,[5,3,2])
#     if t == ['red']:
#         cnt1 += 1
#     elif t == ['green']:
#         cnt2 += 1
#     else:
#         cnt3 += 1
# print(f"Red: {cnt1}, Green: {cnt2}, Blue: {cnt3}")

# task-9