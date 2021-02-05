import requests

while True:
    response = requests.get("http://httpbin.org/")
    response.encoding = "utf-8"
