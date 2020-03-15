import requests

url = 'https://www.baidu.com'
# 定制请求头，使用标准的浏览器才有反馈
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36'
}
#
# response = requests.get(url=url, headers=headers)
#
# print(response.headers)
# print(response.cookies)
# print(response.cookies['BAIDUID'])


url = 'http://httpbin.org/cookies'
# 两种字典的写法都ok
# cookies = dict(cookies_are = 'hello imooc')
cookies = {'cookies_are': 'hello imooc'}
response = requests.get(url=url, cookies=cookies)
print(response.text)
