# x = True
# country_counter = {}
#
#
# def addone(country):
#     if country in country_counter:
#         country_counter[country] += 1
#     else:
#         country_counter[country] = 1
#
#
# addone('China')
# addone('Japan')
# addone('china')
#
# print(len(country_counter))
# print(str(country_counter))


# age = int(input("请输入你家狗狗的年龄: "))
# # print("")
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("对应人类年龄: ", human)
#
# # 退出提示
# input("点击 enter 键退出")


# 程序演示了 == 操作符
# 使用数字
# print(5 == 6)
# # 使用变量
# x = 5
# y = 8
# print(x == y)

# !/usr/bin/python3

# count = 0
# while count < 5:
#     print(count, " 小于 5")
#     count = count + 1
# else:
#     print(count, " 大于或等于 5")


# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for i in range(len(a)):
#     print(i, a[i])

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')