import json
import urllib.request
import urllib.error

HOST = "georgiademolitionandremoval.com"
KEY = "24c96ea4d2324f9f8c62ffdbbce9d7da"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

# Priority URLs to ping
URLS = [
    f"https://{HOST}/",
    f"https://{HOST}/about/",
    f"https://{HOST}/contact/",
    f"https://{HOST}/faqs/",
    f"https://{HOST}/locations/",
    f"https://{HOST}/services/",
    f"https://{HOST}/services/residential-demolition/",
    f"https://{HOST}/services/core-demolition/",
    f"https://{HOST}/services/specialized-demolition/",
    f"https://{HOST}/services/ancillary-demolition/",
    f"https://{HOST}/services/post-demolition/",
    f"https://{HOST}/locations/atlanta/",
    f"https://{HOST}/locations/augusta/",
    f"https://{HOST}/locations/columbus/",
    f"https://{HOST}/locations/savannah/",
    f"https://{HOST}/locations/athens/",
    f"https://{HOST}/locations/macon/",
    f"https://{HOST}/locations/sandy-springs/",
    f"https://{HOST}/locations/roswell/",
    f"https://{HOST}/locations/albany/",
    f"https://{HOST}/locations/marietta/",
]

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": KEY_LOCATION,
    "urlList": URLS
}

data = json.dumps(payload).encode("utf-8")
endpoints = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow"
]

print(f"Submitting {len(URLS)} URLs to IndexNow...")

for endpoint in endpoints:
    req = urllib.request.Request(
        endpoint,
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "IndexNow-Client/1.0"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f"[{endpoint}] Response: {resp.status} {resp.reason}")
    except urllib.error.HTTPError as e:
        print(f"[{endpoint}] HTTPError: {e.code} {e.reason} - {e.read().decode('utf-8', errors='ignore')}")
    except Exception as e:
        print(f"[{endpoint}] Error: {e}")
