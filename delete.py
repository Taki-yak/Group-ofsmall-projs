import requests
response = requests.post("https://httpbin.org/post", json={"key": "value"})
print(response.json())  # Show the response in JSON format