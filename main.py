import requests
from twilio.rest import Client

api_key = "bf7d8c46d84c698da1fa23a5c5345682"
api_endpoints ="https://api.openweathermap.org/data/2.8/onecall"
account_sid = "AC4192c44a227c5b602457a89de7382d03"
auth_token = "21606e4adbe3ea6ab447de7fcf20dbd4"




STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "5fb90610b5a8472a8267dcb940abd52b"
STOCK_API_KEY = "EOL03JKQC2IP6GEA"


stock_params= {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
response=requests.get(STOCK_ENDPOINT, params=stock_params)
data=response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(f"yesterday_closing_price: {yesterday_closing_price}")

day_before_yesterday_data = data_list[1]
day_before_yesterday_data = day_before_yesterday_data["4. close"]
print(f"day_before_yesterday_data:  {day_before_yesterday_data}")

difference=abs(float(yesterday_closing_price) - float(day_before_yesterday_data))
up_down = None
if difference>0:
    up_down = "🔺"
else:
    up_down = "🔻"


diff_percent = round((difference/ float(yesterday_closing_price))*100)
print(f"Percentage: {diff_percent}")

if diff_percent>5:
       news_params={
              "apikey": NEWS_API_KEY,
              "qInTitle": STOCK,
       }
       news_response = requests.get(NEWS_ENDPOINT, params=news_params)
       articles = news_response.json()["articles"]
       three_articles = articles[:3]



       formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadlines: {article['title']}. \nBreief: {article['description']}" for article in three_articles]
       print(formatted_articles)


       client= Client(account_sid,auth_token)
       for article in formatted_articles:
            message = client.messages.create(
                body= article,
                from_="+14846991178",
                to="+919026815037"
            )
