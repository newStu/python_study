

# 装饰器 - 函数增强
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        print(f"调用 {args} {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@log_decorator
def greet(name, age):
    return f"Hello, {name}, you are {age} years old"


print(greet("wzy", age=17))