# 列表可变
lst = [1, 2, 3]
lst[0] = 10  # ✅ 可以修改

# 字符串不可变
s = "hello"
# s[0] = "H"  # ❌ TypeError

# 元组不可变
tup = (1, 2, 3)
# tup[0] = 10  # ❌ TypeError