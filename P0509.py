# salarySum = 0
# salarys = []
# for i in range(4):
#     s = input("请输入一共4名员工的薪资:>")
#
#     if s.upper() == 'Q':
#         print("录入完成，退出")
#         break
#     if float(s) < 0:
#         continue
#
#     salarys.append(float(s))
#     salarySum += float(s)
#
# else:
#     print("您已经全部录入4名员工的薪资")
#
# print("录入薪资：", salarys)
# print("平均薪资{0}".format(salarySum/4))


# 字典推导式
my_text = "i love you, i love sxt, i love shamrock"
char_count = {c: my_text.count(c) for c in my_text}
print(char_count)
