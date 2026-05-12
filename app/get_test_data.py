import requests
import re
import json

url = "https://www.google.com/maps/place/Zone+Gym/@51.5946481,-0.1129059,17z/data=!3m1!4b1!4m6!3m5!1s0x48761be146572445:0x2d37acbbea14b2ad!8m2!3d51.5946481!4d-0.1129059!16s%2Fg%2F1yh9tz67v?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI2MDUwMi4wIKXMDSoASAFQAw%3D%3D"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/147.0.0.0 Safari/537.36"
    )
}

r = requests.get(url, headers=headers)

text = r.text

# PHONE
phone_match = re.search(
    r'tel:(\+[0-9]+)',
    text
)

phone = (
    phone_match.group(1)
    if phone_match else None
)

# WEBSITE
website_match = re.search(
    r'\["(https://[^"]+)"\,"([^"]+)"\,null\,null',
    text
)

website = (
    website_match.group(1)
    if website_match else None
)

# RATING
rating_match = re.search(
    r'\[null,null,null,null,null,null,null,([0-9.]+)\]',
    text
)

rating = (
    rating_match.group(1)
    if rating_match else None
)

# NAME
name_match = re.search(
    r'"0x[a-zA-Z0-9:]+","([^"]+)"',
    text
)

name = (
    name_match.group(1)
    if name_match else None
)

result = {
    "name": name,
    "phone": phone,
    "website": website,
    "rating": rating
}

print(json.dumps(result, indent=4))