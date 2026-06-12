def add_student(students):
    try:
        name = input("请输入学生姓名：")
        score = int(input("请输入学生成绩："))
        students[name] = score
        print("添加成功！", name, "的成绩是", score)
    except ValueError:
        print("成绩必须是数字，添加失败！")

def show_all(students):
    if len(students) == 0:
        print("还没有学生成绩，请先添加。")
    else:
        print("\n所有学生成绩：")
        for name, score in students.items():
            print(name, ":", score, "分")

def search_student(students):
    name = input("请输入要查询的学生姓名：")
    if name in students:
        print(name, "的成绩是：", students[name], "分")
    else:
        print("未找到该学生。")

def delete_student(students):
    name = input("请输入要删除的学生姓名:")
    if name in students:
        del students[name]
        print("已删除", name, "的成绩")
    else:
        print("未找到该学生，请重新输入。")

def calc_average(students):
    if len(students) == 0:
        print("还没有学生成绩，无法计算。")
    else:
        total = sum(students.values())
        avg = total / len(students)
        print("平均分：", avg)
        print("最高分：", max(students.values()))
        print("最低分：", min(students.values()))

def save_to_file(students):
    if len(students) == 0:
        print("没有数据可保存。")
    else:
        with open("students.txt", "w", encoding="utf-8") as f:
            for name, score in students.items():
                f.write(name + "," + str(score) + "\n")
        print("保存成功！")

def load_from_file():
    students = {}
    try:
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                name, score = line.strip().split(",")
                students[name] = int(score)
        print("读取成功！共加载", len(students), "条记录。")
    except FileNotFoundError:
        print("未找到存档文件。")
    return students

def main():
    students = {}
    
    while True:
        print("\n===== 学生成绩管理系统 =====")
        print("1. 添加学生成绩")
        print("2. 查看所有成绩")
        print("3. 查询学生成绩")
        print("4. 计算平均分")
        print("5. 保存到文件")
        print("6. 从文件读取")
        print("7. 退出系统")
        print("8.删除学生成绩")
        
        choice = input("请选择功能（1-7）：")
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_all(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            calc_average(students)
        elif choice == "5":
            save_to_file(students)
        elif choice == "6":
            students = load_from_file()
        elif choice == "8":
            delete_student(students)
        elif choice == "7":
            print("谢谢使用，再见！")
            break
        else:
            print("输入错误，请重新选择！")
main()

import math
def get_number():
    while True:
        try:
            num = int(input("数字:"))
            return num
        except ValueError:
            print("输入错误")
def main():
    while True:
        print("1.倍数")
        print("2.平方")
        print("3.退出")
        print("4.开平方根")
        choice = input("请选择:")
        if choice == "1":
            num = int(input("数字:"))
            print("结果是:", num * 2)
        elif choice == "2":
            print("结果是:", math.pow(num, 2))
        elif choice == "4":
            print("结果是:", math.sqrt(num))
        elif choice == "3":
            print("退出")
            break