import time


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 好处：
# 1. 惰性计算：按需生成值，节省内存
# 2. 无限序列：可以表示无限长的斐波那契数列
# 3. 状态保持：自动记住执行状态
# 4. 可迭代：支持for循环和next()调用
# 示例：获取前10个斐波那契数
print("前10个斐波那契数:")
for i, num in zip(range(10), fibonacci()):
    print(f"F{i}: {num}")

fib = fibonacci()
print(next(fib))  # 0
print(next(fib))  # 1
print(next(fib))  # 1
print(next(fib))  # 2


# 生成器表达式示例
squares = (x**2 for x in range(10))
print("前5个平方数:")
for i, num in zip(range(5), squares):
    print(f"Square {i}: {num}")


# 文件读取生成器
def read_large_file(file_path):
    """逐行读取大文件"""
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


# 模拟数据流生成器
def data_stream():
    import random

    while True:
        yield {"timestamp": time.time(), "value": random.random() * 100}


# 管道式生成器
def filter_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n


def square(numbers):
    for n in numbers:
        yield n**2


# 使用管道
numbers = range(20)
result = square(filter_even(numbers))
print(list(result))  # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

