import os

def build_save():
    pyname = input("请输入文件名（不加后缀）：")
    os.system(f'echo. > {pyname}.py')
    os.system(f'notepad {pyname}.py')
    print(f'{pyname}.py 已创建并打开')

build_save()