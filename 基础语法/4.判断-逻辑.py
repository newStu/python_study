age = 18
old = 40


print("--------普通--------")
if age > old:
    print("age > old")


if age < old:
    print("age < old")


print("--------is == or and not--------")
my_list = [1, 2, 3]
his_list = [1, 2, 3]
# is 和 == 的区别是is比较的是内存地址，==比较的是值，is比==要严格
if my_list == his_list:
    print("my_list == his_list")

if my_list is his_list:
    print("my_list is his_list")

if my_list is his_list or my_list == his_list:
    print("my_list or his_list")

if my_list is his_list and my_list == his_list:
    print("my_list and his_list")

if my_list is not his_list:
    print("my_list is not his_list")

if my_list != his_list:
    print("my_list != his_list")


print("--------不同类型对比--------")
my_set = {1, 2, 3}
my_tuple = (1, 2, 3)
if my_list == my_set:
    print("my_list == my_tuple")

if my_list == my_tuple:
    print("my_list == my_tuple")
