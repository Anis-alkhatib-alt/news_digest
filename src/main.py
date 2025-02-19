import requests as r

from send_email import send_email

topic = "business"

api_key = "ab9b8f9933404880b5d704189a13d420"
url = (
    "https://newsapi.org/v2/top-headlines?"
    "country=us&"
    "language=en&"
    f"category={topic}&"
    f"apiKey={api_key}"
)
request = r.get(url)
content = request.json()
body = ""

for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body += (
            article["title"]
            + "\n"
            + article["description"]
            + "\n"
            + article["url"]
            + 2 * "\n"
        )

send_email(body)
