# scores = {
#     'ali':85,
#     'vali':92,
#     'hasan':78
# }
# mx = -999999
# mx_name = ''
# for i, j in scores.items():
#     if j > mx:
#         mx = j
#         mx_name = i
# print(mx_name, mx)


# task-1




# dictionary1 = {}
# n = int(input())
# for i in range(1, n+1):
#     dictionary1[i] = i * i

# print(dictionary1.items())


# task-2




# key1 = ['name', 'age', 'city']
# value1 = ['ali', 25, 'dushanbe']
# dict1 = {}
# for i in range(len(key1)):
#     dict1[key1[i]] = value1[i]
# for i, j in dict1.items():
#     print(i, j)

# task-3




# person = {
#     'name': 'Ali',
#     'age': 25,
#     'city': 'Dushanbe'
# }
# person['prefession'] = 'Engineer'
# print(person)

# task-4



# person = {
#     'name': 'Ali',
#     'age': 25,
#     'city': 'Dushanbe'
# }
# print(person['city'])

# task-5




# person = {
#     'name': 'Ali',
#     'age': 28,
#     'city': 'Dushanbe'
# }
# person['age'] = 30
# print(person)

# task-6



# colors = {
#     'red': '#FF0000',
#     'green': '#00FF00',
#     'blue': '#0000FF'
# }
# for key, value in colors.items():
#     print(f"{key}---> {value}")

# task-7



# person = {
#     'name': 'Ali',
#     'age': 25,
#     'city': 'Dushanbe'
# }
# b = False
# for key in person.keys():
#     if 'age' == key:
#         b = True
# if b:
#     print('key is exist')
# else:
#     print('key is not exist')

# task-8



# keys = [
#     'name',
#     'age',
#     'city'
# ]
# value = [
#     'ali',
#     25,
#     'dushanbe'
# ]
# person = {}
# for i in range(len(keys)):
#         person[keys[i]] = value[i]
# print(person)

# task-9



# d1 = {
#     'a' : 1,
#     'b' : 2,
# }
# d2 = {
#     'b' : 3,
#     'c' : 4
# }
# res = d1.copy()
# for key, value in d2.items():
#     res[key] = value
# print(res)

# task-10