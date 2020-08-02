import requests
# GET Request
payload = {"firstName": "John", "lastName": "Smith"}
r = requests.get("https://httpbin.org/get", params=payload)
# Show results in json
print(r.text)
# Show reseults in bytes
print(r.content)
# Show requests status code
print(r.status_code)
# Show requested url
print(r.url)


# POST Request
payload = {"firstName": "John", "lastName": "Smith"}
r = requests.post("https://httpbin.org/post", data=payload)
# Show results in json
print(r.text)
# Show reseults in bytes
print(r.content)
# Show requests status code
print(r.status_code)
# Show requested url
print(r.url)