# 多重赋值
a, b, c = 1, 2, 3

# 交换变量
a, b = b, a  # 不需要临时变量！

# 解包列表/元组
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)  # 1
print(middle)  # [2, 3, 4]
print(last)  # 5


# 强类型 - 严格的类型检查, 需要转了后才能拼接
result = "价格：" + str(100) 




print("--------上下文管理器（with 语句）--------")

# 自动管理资源，确保正确关闭 
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
readme_path = os.path.join(script_dir, "..", "README.md")
with open(readme_path, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
# 文件会自动关闭

# 等价于
file = open(readme_path, "r", encoding="utf-8")  # 正确  
try:
    content = file.read()
finally:
    file.close()


print("--------zip--------")
# 一次循环多个可迭代对象
for i, j, k in zip([1, 2, 3], {4, 5, 6}, ("a", "b", "c", "d")):
    print(i, j, k)



# 简单的实现逻辑，将多个可迭代对象使用iter函数进行转化，然后调用next函数获取下一个元素
range_iter = iter(range(10))  # 调用 range.__iter__()
print(next(range_iter))  # 调用 range.__next__()


# 字典的zip用法
keys = ["name", "age", "sex"]
values = ["张三", 25, "男"]
for key, value in zip(keys, values):
    print(f"{key}: {value}")
