import requests
# get方法带参数
data = {'key1':'value1','key2':'value2'}

response = requests.get('http://httpbin.org/get', params=data)

# 返回的几种类型
# print(response.url)

# 查看返回头，是headers
# print(response.headers)
# 查看请求头，可以自定义
print(response.request.headers)

# print(response.text)

# 返回状态码
print(response.status_code)