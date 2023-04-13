import requests
import os

res = requests.post(
    "https://api.short.io/links",
    json={
        "domain": os.getenv("domain"),
        "originalURL": "http://yourlongdomain.com/yourlonglink",
        "path": "test",
    },
    headers={
        "authorization": os.getenv("short_API_KEY"),
        "content-type": "application/json",
    },
)

res.raise_for_status()
data = res.json()

print(data)
