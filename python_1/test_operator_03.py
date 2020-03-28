'''
练习3：输入年份判断是不是闰年。

能被4整除却不能被100整除 或 能被400整除的年份是闰年
'''
year = int(input("输入年份："))

is_leap = (year % 4 == 0 and year %100 != 0) or year % 400 == 0

print('%d 年是闰年吗？%s' % (year, is_leap))