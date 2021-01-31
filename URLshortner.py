# pip install pyshorteners

import pyshorteners

url = input("Enter URL : ")

short_url = pyshorteners.Shortener().tinyurl.short(url)

print("Shorted URL :- ", short_url)
