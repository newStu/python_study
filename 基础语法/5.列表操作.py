my_list = [1, 2, 3, 4, 5]

print("---------list 操作---------")
# list[start:end:step] 包含start不包含end
print(my_list[0]) # 1
print(my_list[-1]) # 5
print(my_list[0:3]) # [1, 2, 3]
print(my_list[:3]) # [1, 2, 3]
print(my_list[1:]) # [2, 3, 4, 5]
print(my_list[:]) # [1, 2, 3, 4, 5]
print(my_list[::-1]) # [5, 4, 3, 2, 1]
print(my_list[::2]) # [1, 3, 5]
print(my_list[::-2]) # [5, 3, 1]



print("---------列表推导式---------") 
# 列表推导式（Python 特色）
print([x * 10 for x in my_list if x % 2 == 0])