import requests

api_key = "f7b67416196f4d6283cc71a7048fdccd"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-18" \
       "&sortBy=publishedAt&apiKey=" \
       "f7b67416196f4d6283cc71a7048fdccd"

# Make request
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the articles description and title
for article in (content["articles"]):
    print(article["description"])
    print(article["title"])