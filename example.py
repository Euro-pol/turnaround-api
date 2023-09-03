import requests

body = {
    "sitekey": "0x4AAAAAAAHWfmKCm7cUG869",
    "url": "https://modrinth.com/auth/sign-up",
    "invisible": True,
}

r = requests.post("http://127.0.0.1:5000/solve", json=body)
token = r.json()["token"]
print(f"Solved :: {token}")
