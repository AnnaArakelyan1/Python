url1 = "https://jsonplaceholder.typicode.com/posts/100"
response = requests.get(url1)
if response.status_code == 200:
    print("Response JSON:", response.json())
else:
    print("Failed to retrieve data:", response.status_code)


data2 = {
    "title": "Updated Title",
    "body": "Updated body text.",
    "userId": 1
}

response2 = requests.put(url1, json=data2)

if response2.status_code == 200:
    print("Post updated successfully.")
    updated_post = response2.json()
    print("Updated Post Data:", updated_post)
else:
    print("Failed to update post:", response2.status_code)

