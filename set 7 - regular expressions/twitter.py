# Set 7 Class - Regular Expressions

# Intro to get url
    # url = input("URL: ").strip()

    # # username = url.replace("https://twitter.com/","")
    # username = url.removeprefix("https://twitter.com/")
    # print(f"Username: {username}")

# Using re library
import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")