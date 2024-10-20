import requests
from send_email import send_email
API_KEY = "38bd1d10da0f471cb272f7234badb2c4"

url = ("https://newsapi.org/v2/everything?q=tesla"
       "&from=2024-09-20&sortBy=publishedAt&apiKey="
       "38bd1d10da0f471cb272f7234badb2c4")

# Make a request
request = requests.get(url)

# Get dictionary
content = request.json()

news_body = ""
# Access the article titles and descriptions
for article in content["articles"]:
    news_body = news_body + article["title"]+ "\n" + article["description"] + 2*"\n"

# Update variable to UTF-8 Encoding
news_body = news_body.encode("UTF-8")

email_message = f"""\
Subject: Daily News 

{news_body}
"""
send_email(email_message)

