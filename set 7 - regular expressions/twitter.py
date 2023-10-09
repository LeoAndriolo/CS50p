# Set 7 Class - Regular Expressions

# Intro to get url
    # url = input("URL: ").strip()

    # # username = url.replace("https://twitter.com/","")
    # username = url.removeprefix("https://twitter.com/")
    # print(f"Username: {username}")

# Using re library
import re

url = input("URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE): # ?: -> Non-capturing this () syntax
    print(f"Username: {matches.group(1)}")