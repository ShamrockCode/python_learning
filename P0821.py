# def change(a):
#     print(id(a))  # 指向的是同一个对象
#     a = 10
#     print(id(a))  # 一个新对象
#
#
# a = 1
# print(id(a))
# change(a)
# print(id(a))

# 可写函数说明
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1, 2, 3, 4])
#     print("函数内取值: ", mylist)
#     return
#
#
# # 调用changeme函数
# mylist = [10, 20, 30]
# print("初始列表值：", mylist)
# changeme(mylist)
# print("函数外取值: ", mylist)

# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出；")
#     print(arg1)
#     print(vartuple)
#
#
# printinfo(70, 60, 50)


# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print("函数内：", total)
#     return total
#
# total = sum(10, 20)
# print("函数外：", total)

# vec1 = [2, 4, 6]
# vec2 = [4, 3, -9]
# print([x * y for x in vec1 for y in vec2])

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# print([[row[i] for row in matrix] for i in range(4)])
result = []
for i in range(4):
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    result.append(new_row)
print(result)
