# Peticiones a APIs

from os import system

if system("clear") != 0:
    system("cls")

# 1. Sin dependencias

import urllib.request
import json

# api_posts = "https://jsonplaceholder.typicode.com/posts"
# try:
#     response = urllib.request.urlopen(api_posts)
#     data = response.read()
#     json_data = json.loads(data.decode("utf-8"))
#     print(json_data)
#     response.close()
# except urllib.error.URLError as e:
#     print(f"Error: {e.reason}")


# 2. Con dependencias (requests)
import requests

print("\nGET: ")
try:
    api_posts = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(api_posts)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

print("\nPOST: ")
try:
    api_posts = "https://jsonplaceholder.typicode.com/posts"
    input = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(api_posts, json=input)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
