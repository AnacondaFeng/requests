import requests

response = requests.get(url='http://httpbin.org/ip')
# 返回json数据，使用response.json
data = response.json()

print(data)
print(data['origin'])