# how to use an API from the web

import requests

url = "http://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)


print(response) # do we get 200 - all good?

print(response.text)

print(response.json())

todo = response.json()