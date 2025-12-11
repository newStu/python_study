print("---------普通循环---------")
for i in range(3):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")



print("---------list循环---------") 
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(f"list: {i}")



print("--------set循环----------") 
my_set = {1, 2, 3, 4, 5}
for i in my_set:
    print(f"set: {i}")




print("----------元组循环--------")
my_tuple = (1, 2, 3, 4, 5)
for i in my_tuple:
    print(f"tuple: {i}")




print("----------字典循环--------")
my_dict = {"name": "wzy", "age": 18, "score": 100}
for key, value in my_dict.items():
    print(f"{key} is {value}")



print("---------字符串循环---------")
my_str = "hello world"
for i in my_str:
    print(f"str: {i}")





print("---------break 在 match的特殊情况---------")
"""
break 会跳出最近的那层循环
Python 3.10+ 支持 match-case 语句
"""
for i in range(3):
    match i:
        case 0:
            print("first")
            break
        case 1:
            print("second")
        case 2:
            print("third")


for i in range(2):
    for j in range(3):
        match j:
            case 0:
                print("first")
                break
            case 1:
                print("second")
            case 2:
                print("third")




print("---------while循环---------")
# while 循环。并不存在do-while循环
sum = 1
while sum < 20:
    sum += 1
    print(f"sum: {sum}")
