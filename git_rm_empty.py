import os
def remove_empty_folders(dir):
    if not os.path.exists(dir):
        print(f"【失败】 {dir}不存在")
        return
    count = 0
    for item in os.listdir(dir):
        item_path = os.path.join(dir, item)
        try:
            if os.path.isdir(item_path) and len(os.listdir(item_path)) == 0:
                os.rmdir(item_path)
                print(f"已删除空文件夹:{item_path}")
                count = count + 1
        except PermissionError:
            pass
    if count == 0:
        print("没有找到文件夹")
    else:
        print(f"共删除{count}个空文件夹")