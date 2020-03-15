import requests

# 通过get方法来请求数据，requests.get
response = requests.get(url='http://www.qq.com')
print(response.text)

# 通过post方法请求数据
# 构造发送的数据，使用字典的方式，插入data参数
data = {'name': 'imooc'}
response = requests.post('http://httpbin.org/post', data=data)
print(response.text)
