import requests

url = "https://jsonplaceholder.typicode.com/posts"
response=requests.get(url)   

if response.status_code == 200:
    posts = response.json()

    bodies = [post['body'] for post in posts]

    for body in bodies:
        print("Body (Raw):")
        print(repr(body))

        newline_count = body.count('\n') 
        if newline_count > 3: 
            print(f"Body with more than 3 newlines:\n{body}\n")
else:
    print("Failed to retrieve posts:", response.status_code)

