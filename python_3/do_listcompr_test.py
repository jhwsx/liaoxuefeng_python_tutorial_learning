# L1 = ['Hello', 'World', 18, 'Apple', None] 使用列表生成式，把 L1 的元素转为小写
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [element.lower() for element in L1 if isinstance(element, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')