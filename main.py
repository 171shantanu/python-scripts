import requests

response = requests.get("https://httpbin.org/get")

res_json = response.json()
del res_json['origin']
print(res_json) 