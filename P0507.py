# num = input("输入一个数字:")
# if int(num) < 10:
#     print(num)

# for x in range(5):
#     for y in range(5):
#         print(x,end="\t")
#     print("\n")

# 打印九九乘法表
# for m in range(1, 10):
#     for n in range(1, m + 1):
#         print("{0}*{1}={2}".format(m, m, (m * n)), end="\t")
#     print()


# 输入员工的薪资，若薪资小于0则重新输入。
#  最后打印出录入员工的数量和薪资明细，以及平均薪资
empNum = 0
salarySum = 0
salarys = []

while True:
    s = input("请输入员工的薪资（按Qq结束）")

    if s.upper() == 'Q':
        print("录入完成，退出")
        break

    if float(s)<0:
        continue

    empNum += 1
    salarys.append(float(s))
    salarySum += float(s)

print("员工数{0}".format(empNum))
print("录入薪资：",salarys)
print("平均薪资{0}".format(salarySum/empNum))