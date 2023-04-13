import requests
import os
url = "https://api.short.io/links/expand"

querystring = {"domain":os.getenv("domain"),"path":"gba"}

headers = {
    'accept': "application/json",
    'authorization': os.getenv("short_API_KEY")
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json()["idString"])