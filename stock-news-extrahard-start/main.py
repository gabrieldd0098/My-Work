import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://www.newsapi.org/v2/everything"

STOCK_API_KEY = "AK9991818"
NEWS_API_KEY = "1cfgh9910sf"
TWILIO_ACCOUNT_SID = "VBCADF5680880BC"
TWILIO_AUTH_TOKEN = "4cbfrngh7674"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
p_difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

diff_perc = p_difference / float(yesterday_closing_price) * 100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if diff_perc > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_resp = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_resp.json()["articles"]
    three_articles = articles[:3]

    formatted = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for article in three_articles:
        message = client.messages.create(article,"+91483257","+91483257")

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
#Optional: Format the SMS message
