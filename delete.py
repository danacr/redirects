import requests
import os

url = "https://api.short.io/links/LINK_ID"

headers = {"authorization": os.getenv("short_API_KEY")}

response = requests.request("DELETE", url, headers=headers)

print(response.text)
