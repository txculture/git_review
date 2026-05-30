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

# DAY23小项目：成绩统计
scores = [85,92,78,95,88]
total = 0
for s in scores:
    total =total + s
print("平均分:", total / len(scores))
print("最高分:", max(scores))

#DAY 24 小项目：BMI计算器
height = float(input("请输入身高(米):"))
weight = float(input("请输入体重(公斤):"))
bmi = weight / (height ** 2)
print("BMI:",bmi)
if bmi < 18.5:
    print("偏瘦")
elif bmi < 24:
    print("正常")
else:
    print("偏胖")

#Day 25小项目：随机猜数字
import random
secret = random.randint(1,100)
guess = 0
count = 0
print("猜一个1-100的数字:")
while guess =! secret:
    guess = int(input("猜一个数字"))
    count = count + 1
    if guess > secret:
        print("太大了")
    elif guess < secret:
        print("太小了")
    else:
        print("答对了")
        print("你猜了:", count, "次")