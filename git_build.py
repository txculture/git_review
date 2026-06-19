import os

def git_build():
    pyname = input("请输入文件名（加后缀）：")
    os.system(f'echo. > {pyname}')
    os.system(f'notepad {pyname}')
    print(f'{pyname} 已创建并打开')

git_build()