"""https://www.dataquest.io/blog/api-in-python/"""

import requests
import json

response = requests.get("https://api-server.dataquest.io/economic_data/countries?filter_by=region=Sub-Saharan%20Africa")
print(response.status_code)

data = response.json()

def jprint(obj):
    text = json.dumps(obj, sort_keys = True, indent = 4)
    print(text)

jprint(response.json())