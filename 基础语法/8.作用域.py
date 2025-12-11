x = 10  # 全局变量

# 局部变量
def modify():
    x = 20  # 创建局部变量，不会修改全局的 x
    print("局部:", x)

modify()  # 输出: 局部: 20
print("全局:", x)  # 输出: 全局: 10



# 要修改全局变量需要声明
def modify_global():
    global x
    x = 30

modify_global()
print("修改后全局:", x)  # 输出: 修改后全局: 30



count = 10
# nonlocal 声明变量来自外层作用域
def outer():
    count = 0
    
    def inner():
        nonlocal count    # ✅ 声明count来自外层作用域
        count += 1
        return count
    
    return inner

counter = outer()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
print(count) # 10