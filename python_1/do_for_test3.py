# 用下面的代码来实现1~100之间的偶数求和
sum = 0
for i in range(2, 101, 2):
    sum += i
print(sum) # 2550

sum = 0
for i in range(1, 101):
    if (i & 1 == 0):
        sum += i
print(sum) # 2550

# 用下面的代码来实现1~100之间的奇数求和
sum = 0
for i in range(1, 101, 2):
    sum += i
print(sum) # 2500

sum = 0
for i in range(1, 101):
    if (i & 1 != 0):
        sum += i
print(sum) # 2500

