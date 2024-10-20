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

if "articles" not in content or not content["articles"]:
    print("No articles found or 'articles' key missing in the response.")
    exit()

news_body = ""
# Access the article titles and descriptions
for article in content["articles"]:
    if  article["title"] is not None and article["description"] is not None:
        news_body = news_body + article["title"]+ "\n" + article["description"] + 2*"\n"

# Update variable to UTF-8 Encoding
news_body = news_body.encode("utf-8", errors="ignore").decode("utf-8")

email_message = f"""\
{news_body}
"""
send_email(email_message)

