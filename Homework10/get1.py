import requests

url = "https://jsonplaceholder.typicode.com/posts"
response=requests.get(url)   

if(response.status_code==200):
    posts=response.json()
    titles=[post['title'] for post in posts]
    print("All titles:")
    for title in titles:
        print(title)
else:
    print("Failed to retrieve posts:", response.status_code)

print("\n\nTitles that contain 6 words")
for title in titles:
    words=title.split()
    if(len(words)==6):
       print(words)
