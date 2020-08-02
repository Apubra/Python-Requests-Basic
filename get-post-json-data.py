import requests

# POST Json Data(Send data)
data = {'firstName': 'Json'}

r = requests.post('https://httpbin.org/post', json=data)

print(r.text)

# GET Json Data(Get data)
r = requests.get('https://api.github.com/events')
events = r.json()
print(events[0]['id'])