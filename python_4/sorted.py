# sorted 函数

# 对 list 进行从小到大排序
print(sorted([36, -3, 1, 20, -5]))  # [-5, -3, 1, 20, 36]
# 对 list 进行从大到小排序
print(sorted([36, -3, 1, 20, -5], reverse=True))  # [36, 20, 1, -3, -5]
# 对 list 按绝对值从小到大排序
print(sorted([36, -3, 1, 20, -5], key=abs))  # [1, -3, -5, 20, 36]