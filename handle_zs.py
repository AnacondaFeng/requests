import requests

url = 'https://requestb.in/'
#我们通过verify关闭了ssl证书验证选项
response = requests.get(url=url,verify=False)
print(response.text)