import requests
def check_website():
    url = input('请输入网址:')
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f'正常 {url}')
        else:
             print(f'警告 {url} 状态码 {response.status_code}')
    except:
        print(f'失败 {url} 无法访问')

check_website()

