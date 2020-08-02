import requests

def response_info(r, *args, **kwargs):
    print(r.status_code, r.url)
    print(r.text)

hooks = {'response': response_info}
# We can hook multiple function using tupple
r = requests.get('https://httpbin.org/get', hooks=hooks)
