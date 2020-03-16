import requests

#带着用户名密码的代理格式,使用的是动态版的
proxy = {
    "http":"http://H08F737BJ83Z121D:7A6B559E63F5BA46@http-dyn.abuyun.com:9020",
    "https":"http://H08F737BJ83Z121D:7A6B559E63F5BA46@http-dyn.abuyun.com:9020",
}

url = 'http://httpbin.org/ip'
for i in range(5):
    #这里设置了代理的关键字proxies
    response = requests.get(url=url,proxies=proxy)
    print(response.text)