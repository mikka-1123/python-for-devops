import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

#print(response.json())

complete_json = response.json()

for username in range(len(complete_json)):
    print(complete_json[username]["user"]["login"])