import requests

# 设置超时时间，在时间内不返回数据就中断，设置2s
response = requests.get('http://www.github.com', timeout = 2)
print(response.status_code)
print(response.text)