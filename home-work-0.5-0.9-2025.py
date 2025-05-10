# shoping = ['yabloko', 'xleb', 'moloko']
# shoping.append('cir')
# shoping.remove('xleb')
# shoping.reverse()
# shoping.insert(1, 'yayca')
# print(shoping)

# task-1



# nums = [1, 2, 3, 2, 4, 2]
# numscopy = []
# numscopy.extend(nums)
# cnt =  numscopy.count(2)
# nums.remove(2)
# print('list orginal -->',nums)
# print('list copy -->',numscopy)
# print('cnt = 2 -->', cnt)

# task-2



# a = [5, 1, 9]
# b = [4, 7, 3]
# a.extend(b)
# a.sort()
# a.pop()
# print('end lsit -->', a)

# task-3



# letters = ['a', 'b', 'd', 'e']
# ind =  letters.index('d')
# # print(ind)
# letters.insert(1, 'c')
# letters.reverse()
# letters.remove('b')
# print(letters)

# task-4



# data = [10, 20, 30]
# data.append(40)
# data.append(50)
# lenght = len(data)
# data.clear()
# print('list -->', data)
# print('lenght -->', lenght)

# task-5




# nums = [7, 2, 9, 3, 5, 1, 8]
# res_nums = []
# for i in nums:
#     if i % 2 == 0:
#         res_nums.append(i)
# res_nums.sort()
# res_nums.append(10)
# res_nums.append(12)
# res_nums.reverse()
# print(res_nums)

# task-6



# mixed = [3, 'hi', 5, 'hello', 2, 'hi']
# cnt = mixed.count('hi')
# # print(cnt)
# for i in mixed:
#         if i == 'hi':
#                 mixed.remove(i)
# mixed.append('bye')
# mixed.append(0)
# ind =  mixed.index('hello')
# # print(ind)
# mixed.insert(2, 'welcome')
# print(mixed)

# task-7



# items = ['pen', 'book', 'pen', 'ruler', 'pen']
# copyitems = []
# copyitems.extend(items)
# items.remove('pen')
# items.remove('pen')
# items.remove('pen')
# items.insert(1, 'notebook')
# print(items)
# print(copyitems)

# task-8



# a = [3, 8, 1]
# b = [4, 2, 7]
# c = []
# c.extend(a)
# c.extend(b)
# c.remove(min(c))
# c.remove(max(c))
# c.sort()
# lenght = len(c)
# # print(lenght)
# c.insert(2, 'done')
# print(c)

# task-9



# values = [10, 20, 30, 40, 50]
# removed = values.pop(2)
# values.insert(0, removed)
# values.append(removed * 2)
# values.reverse()
# print(values)


# task-10