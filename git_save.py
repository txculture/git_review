import os

def git_save():
    filename = input("请输入要保存的文件名（不加后缀）：")
    message = input("请输入提交信息：")
    os.system(f"git add {filename}.py")
    os.system(f'git commit -m "{message}"')
    os.system("git push")
    print(f" {filename}.py 已提交并推送到 GitHub")

git_save()