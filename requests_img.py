import requests

response = requests.get(url='https://www.imooc.com/static/img/index/logo.png')

# print(response.text)
# 写入模式要用wb方式
with open('imooc.png', 'wb')as f:
    # content返回的是二进制数据
    f.write(response.content)
