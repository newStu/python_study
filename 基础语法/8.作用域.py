x = 10  # 全局变量

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