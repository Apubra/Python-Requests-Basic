import requests

url = 'https://httpbin.org/post'

# Upload Single File
# files = {'file': open('TestFile.txt', 'rb')}

# Upload Multiple Files
files = [
    ('copy1', ('TestFile.txt', open('TestFile.txt', 'rb'), 'csv')),
    ('copy2', ('TestFile.txt', open('TestFile.txt', 'rb'), 'csv'))
]

r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
