'''
练习2：输入圆的半径计算计算周长和面积。
'''
import math
r = float(input("输入圆的半径："))

l = 2 * math.pi * r
s = math.pi * math.pow(r, 2)

print('半径为 %.2f 的圆，周长为 %.2f，面积为 %.2f' % (r, l, s))
