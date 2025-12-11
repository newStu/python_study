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


print("--------上下文管理器（with 语句）--------")

# 自动管理资源，确保正确关闭 
with open("./7.None.py", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
# 文件会自动关闭

# 等价于
file = open("./7.None.py", "r", encoding="utf-8")
try:
    content = file.read()
finally:
    file.close()
