import requests
from send_email import send_email

api_key = "f7b67416196f4d6283cc71a7048fdccd"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-18" \
       "&sortBy=publishedAt&apiKey=" \
       "f7b67416196f4d6283cc71a7048fdccd"

# Make request//
request = requests.get(url)

# Get dictionary with data
content = request.json()

# Access the articles description and title
body = ""
for article in (content["articles"]):
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)



