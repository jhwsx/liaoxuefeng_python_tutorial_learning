# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello, %s!' % name)

i = 0
size = len(L)
while i < size:
    print('Hello, %s!' % L[i])
    i += 1