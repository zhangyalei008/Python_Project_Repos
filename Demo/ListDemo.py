# 创建列表
list1 = ["1", "中国", "jijl", "78989", "pythonClass"]
# 正向输出列表
print(list1[::1])
# 倒着输出列表
print(list1[::-1])
# 访问列表
# 打印指定索引
print(list1[0])
# 打印索引为1开始，索引3前的元素，索引为3的元素不打印
print(list1[1:3])
# 更新列表
list1[1] = "china"
print("新列表索引为2的值：" + list1[1])
# 删除列表元素
# del list1[4]
# pop 移除指定索引的值并返回该值
print(list1.pop(3))
# 查看pop出的值是否还存在
print(list1[3])
print("====================================")
print(list1[::1])

print("-------------------------------------")
rows = 3
cols = 6
matrix = [[0 for col in range(cols)] for row in range(rows)]
print(matrix)
