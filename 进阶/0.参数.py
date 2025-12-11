print("-------------必传参数 位置参数 关键字参数----------------") 
def func(a, b, *args, **kwargs):
    # a 和 b 是必传参数
    # *args 接收多个位置参数
    # **kwargs 接收多个关键字参数
    print(a, b, args, kwargs)
    return a + b + sum(args)


print(func(1, 2, 3, 4, 5, 6, 7, 8, age=9, name=10))
# 参数解包
print(func(*[1, 2, 3, 4, 5, 6, 7, 8], age=9, name=10))


print("-------------必传参数 位置参数----------------")  
def func_args(a, b, *args):
    # a 和 b 是必传参数
    # *args 接收多个位置参数 
    print(a, b, args)
    return a + b + sum(args)


print(func_args(1, 2, 3, 4, 5, 6, 7, 8))
# func_args(1, 2, 3, 4, 5, 6, 7, 8, age = 9, name = 10) # 报错，不支持关键字参数



print("-------------必传参数 关键字参数----------------")  
def func_kwargs(a, b, **kwargs):
    # a 和 b 是必传参数 
    # **kwargs 接收多个关键字参数
    print(a, b, kwargs)
    return a + b + sum(kwargs.values())


print(func_kwargs(1, 2, age = 9, name = 10))
# func_kwargs(1, 2, 3, 4, 5, 6, 7, 8, age = 9, name = 10) # 报错，不支持位置参数

