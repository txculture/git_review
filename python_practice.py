# Day 17 复习题
# 第 4 题：for 循环求 1~100 的和
he = 0
for num in range(1,101):
    he = he + num
print(he)

# DAY 22小项目：通讯录查询
contacts = {"ming":"138001380000","gang":"13700137000"}

def search(name):
    if name in contacts:
        print(name,"的电话是:",contacts[name])
    else:
        print("查无此人")

search("输入通讯录名字查询")