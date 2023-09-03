import requests

body = {
	"sitekey": "0x4AAAAAAAHWfmKCm7cUG869",
	"url": "https://modrinth.com/auth/sign-up",
	"invisible": True
}

r = requests.post("http://localhost:5000/solve", json=body)
token = r.json()["token"]
print("Solved :: " + token)