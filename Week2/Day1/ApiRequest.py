import requests

def try_get(u):
    try:
        r = requests.get(u, timeout=5)
        print("Status:", r.status_code, "URL:", u)
        if r.ok:
            print("JSON keys:", list(r.json().keys()))
    except requests.exceptions.RequestException as e:
        print("REQUEST ERROR:", type(e).__name__, "->", e)

try_get("https://www.boredapi.com/api/activity")
try_get("https://catfact.ninja/fact")
try_get("https://httpbin.org/get")
