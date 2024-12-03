import requests

url = "https://jsonplaceholder.typicode.com/posts"
data1 = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response1 = requests.post(url, json=data1)

if response1.status_code == 201:
    print("First request sent.")
    created_post = response1.json()
    print("Resource created:", response1.json())
else:
    print("Failed to create resource:", response1.status_code)
    print("Response content:", response1.text)
