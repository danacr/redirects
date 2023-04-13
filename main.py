import requests
import os

url = "https://api.short.io/api/links"

querystring = {"domain_id": os.getenv("domain_id"), "limit": "150", "offset": "0"}

headers = {"accept": "application/json", "authorization": os.getenv("short_API_KEY")}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
