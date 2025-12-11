age = 18


# 这里用的是if-elif-else语句
if age > 18:
    print("adult")
elif age > 12:
    print("teenager")
else:
    print("kid")


"""
match语句,有版本限制
类似switch-case语句, 但是这里不需要break,也不会执行后续操作
"""
match age:
    case 18:
        print("adult")
    case 12:
        print("teenager")
    case _:
        print("kid")

# 支持多个条件
match age:
    case 18 | 19:
        print("adult")
    case 12:
        print("teenager")
    case _:
        print("kid")


# 三元运算符
name_type = "adult" if age > 18 else "teenager"
