import requests

s = requests.Session()

userName = {'userName': 'John99'}
location = {'location': 'NewYork'}

setCookieUrl = 'https:httpbin.org/cookies/set'
getCookiesUrl = 'https:httpbin.org/cookies'

s.get(setCookieUrl, params=userName)
s.get(setCookieUrl, params=location)

r = s.get(getCookiesUrl)
print(r.text)