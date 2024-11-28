url1 = "https://jsonplaceholder.typicode.com/posts/100"
response = requests.delete(url1)
if response.status_code == 200:
    print("Resource deleted successfully.")
else:
    print(f"Failed to delete resource. Status code: {response.status_code}, Reason: {response.reason}")
