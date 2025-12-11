# 字符串
name = "wzy"

# 整数
age = 18

# 浮点数
height = 1.75

# 布尔值
is_student = True

# 列表
fruits = ["apple", "banana", "orange"]

# 元组
my_tuple = (1, 2, 3)

# 字典, 注意key一定要用引号抱起来
my_dict = {"name": "wzy", "age": 18, "score": 100}

# 集合
my_set = {1, 2, 3}

# 空值
my_none = None

# 函数
def my_func(name = "wzy"):
  print(f"hello world, {name}")


def my_func2(name, age: int) -> str: 
  print(f"hello world, {name}, {age}")
  return "hello world"


my_func2("wzy", 18)


# lambda 表达式
my_lambda = lambda x: x + 1
print(my_lambda(1))