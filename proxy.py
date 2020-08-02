import requests

proxies = {'https': '84.52.85.201:80'}

r = requests.get('https://httpbin.org/ip', proxies=proxies)
print(r.text)