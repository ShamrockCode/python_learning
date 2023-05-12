# def add(a, b):
#     print("计算两个数之和:>{0}, {1}, {2}".format(a, b, (a + b)))
#     return a + b
#
#
# add(30, 40)
#
#
# def test01(x, y, z):
#     return [x * 10, y * 2, z * 100]
#
#
# print(test01(1, 2, 3))


# b = [10, 20]
#
#
# def f2(m):
#     print("m:", id(m))
#     m.append(30)
#
#
# f2(b)
# print("b:", id(b))
# print(b)


# lambda函数
# f = lambda a, b, c: a + b + c
# print(f)
# print("=====")
# print(f(2, 3, 4))
#
# g = [lambda a:a*2, lambda b:b*3, lambda c:c*4]
# print(g[0](6), g[1](7), g[2](8))

# 测试lambda
# f = lambda a, b, c, d: a * b * c * d
#
#
# def test(a, b, c, d):
#     return a * b * c * d
#
#
# print(f(2, 3, 4, 5))
#
# g = [lambda a:a*2, lambda b:b*3]
# print(g[0](6))

# 测试eval函数
# s = "print('123456')"
# eval(s)
#
a = 10
b = 20
# c = eval("a + b")
# print(c)


dict1 = dict(a=100, b=200)

d = eval("a+b")
print(d)