#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module' # 该模块的文档注释

__author__ = 'Willway Wang' # 作者

import sys

def test():
    args = sys.argv # argv 变量，用 list 存储了命令行的所有参数。argv 至少有一个元素，那就是.py文件的名称
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
# 当我们在命令行运行 hello 模块文件时，Python 解释器把一个特殊变量 __name__ 置为 __main__，而如果
# 在其他地方导入该 hello 模块时，if 判断将失效。
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__ == '__main__':
    test()