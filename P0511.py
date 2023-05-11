# import turtle
#
# t = turtle.Pen()
#
# my_colors = ("red", "green", "yellow", "black")
#
# t.width(4)
# t.speed(10)
#
# for i in range(5):
#     # t.goto(0, 0)
#     # t.circle(100)
#     #
#     # t.goto(0, -100)
#     # t.circle(200)
#     #
#     # t.goto(0, -200)
#     # t.circle(300)
#     t.penup()
#     t.goto(0, -i*10)
#     t.pendown()
#
#     t.color(my_colors[i % len(my_colors)])
#     t.circle(10 + i*10)
# turtle.done()


# ============================================
# 函数

# def test01():
#     print("*" * 10)
#     print("@" * 10)
#
#
# for i in range(10):
#     test01()


def add(a, b):
    print("计算两个数的和:>{0},{1},{2}".format(a, b, (a+b)))
