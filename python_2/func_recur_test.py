# 汉诺塔问题是一个经典的问题。汉诺塔（Hanoi Tower），又称河内塔，源于印度一个古老传说。
# 大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着64片黄金
# 圆盘。大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。并且规定，任
# 何时候，在小圆盘上都不能放大圆盘，且在三根柱子之间一次只能移动一个圆盘。问应该如何操作？
# 参考：https://blog.csdn.net/qq_41705423/article/details/82025409
cnt = 0
def hanoi(n, a, b, c):
    if n == 0:
        return
    else:
        hanoi(n - 1, a, c, b)
        move(1, a, c)
        hanoi(n - 1, b, a, c)
#  打印移动方式：编号，从哪个盘子移动到哪个盘子
def move(n, fm, to):
    global cnt
    print("step %d: move %d from %s->%s" % (cnt, n, fm, to) )
    cnt += 1

hanoi(4, 'A', 'B', 'C')
hanoi(64, 'A', 'B', 'C')
