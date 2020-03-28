# 通过一个“猜数字”的小游戏（计算机出一个1~100之间的随机数，人输入自己猜的数字，
# 计算机给出对应的提示信息，直到人猜出计算机出的数字）来看看如何使用`while`循环。
import random

answer = random.randint(1, 100)
guess_count = 0
while True:
    guess = int(input('输入猜的数字:'))
    guess_count += 1
    if guess < answer:
        print('猜的数偏小')
    elif guess > answer:
        print('猜的数偏大')
    else:
        print('猜对了')
        break
print('你猜了%d次' % guess_count)
if guess_count < 5:
    print('天之骄子')
elif guess_count < 15:
    print('资质平平')
elif guess_count < 25:
    print('资质稍差')
else:
    print('榆木疙瘩')
