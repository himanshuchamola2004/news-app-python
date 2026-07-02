import requests


query = input("What type of news do you want to read?")
api = "69c8e5af59854b55a634a0462af06e57"
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-02-27&sortBy=publishedAt&apiKey={api}"

print(url)

r = requests.get(url)
data = r.json()
print(data)

articles = data["articles"]
for article in articles:
    print(article["title"], article["url"])
    print("\n*******************************\n")

