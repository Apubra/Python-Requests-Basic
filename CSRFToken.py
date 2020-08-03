# import requests
# # POST Request
# payload = {"firstName": "John", "lastName": "Smith"}
# r = requests.post("http://127.0.0.1:8000/dashboards/university", data=payload)
# # Show results in json
# print(r.text)
# # Show reseults in bytes
# print(r.content)
# # Show requests status code
# print(r.status_code)
# # Show requested url
# print(r.url)

import sys
import requests

URL = 'http://127.0.0.1:8000/dashboards/university'

client = requests.session()

# Retrieve the CSRF token first
client.get(URL)  # sets cookie
if 'csrftoken' in client.cookies:
    # Django 1.6 and up
    csrftoken = client.cookies['csrftoken']
else:
    # older versions
    csrftoken = client.cookies['csrf']

login_data = dict(csrfmiddlewaretoken=csrftoken)
r = client.post(URL, data=login_data, headers=dict(Referer=URL))
# r = requests.put('http://127.0.0.1:8000/dashboards/university')
print(r.text)
print(csrftoken)