"""https://www.dataquest.io/blog/api-in-python/"""

import requests 
import json

# GET Request
response = requests.get("http://api.open-notify.org/astros")
print(response.status_code)

def jprint(obj):
    text = json.dumps(obj, sort_keys = True, indent = 4)    # Format Data for readability
    print(text)


jprint(response.json())