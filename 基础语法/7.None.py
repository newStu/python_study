# Python 的 None 相当于 JS 的 null/undefined
value = None
if value is None:  # 推荐用 is 而不是 ==
    print("值是 None")

# 变量未定义会直接报错，不会返回 undefined
# print(undefined_var)  # ❌ NameError