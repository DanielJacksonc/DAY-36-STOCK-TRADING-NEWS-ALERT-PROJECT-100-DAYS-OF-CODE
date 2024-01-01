# import the request module to be able to work with your endpoint
import requests
from twilio.rest import Client


# my constants and endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
percentage = 100
NEWS_API = "f24f3b78d92e4b1fab89b9f4c2b1e23d"

# use need an access key to get an API. get it from the websites
STOCK_PARAMS = {
    "apikey": "HC8VKJW3UESHYWWI",
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
}


NEWS_ACCESS =\
    {
       "q": "tesla",
       "from": 2023-12-29,
       "to": 2023-12-31,
       "sortBy": "publishedAt",
       "apiKey": "f24f3b78d92e4b1fab89b9f4c2b1e23d"
    }

# Twilio account ID
account_sid = "AC38cab02a5a7a01d960e80a2d5556818d"
auth_token = "aaba78296f3267ed1c8717a3de1a5f12"

# import the Tesla API

tesla_api = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS)
tesla_api.raise_for_status()
data = tesla_api.json()
# We can actually use a for loop to itterate through a dict. Here it is
data_list =[v for k,v in data.items()]

yesterdays_data = data_list[0]
yesterdays_closing_price = yesterdays_data['4. close']
day_before_yesterday_data = data[1]
day_before_yesterday_closing_price  = day_before_yesterday_data['4. close']


# find the absolute difference
diff = abs(float(day_before_yesterday_closing_price)-float(day_before_yesterday_data))
percent_dif = (diff /float(yesterdays_closing_price))* percentage
print(percent_dif)


tesla_news = requests.get(url=NEWS_ENDPOINT, params=NEWS_ACCESS)
tesla_news.raise_for_status()
tesla_news = tesla_news.json()
three_news = (tesla_news["articles"][0:3])


for i in three_news:
    title = (i['title'])
    description = (i["description"])

    """we can also perform list comprehension on the above:"""
# formated_list = [new item for item in item_list]
# formated_list = [f"Headlines:{article['title']}.{article['description']}" for article in three_news]

    # Use your Twilio account to send the message
    if percent_dif > 5:
        print(title)
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="+18556121826",
            to="+16466294880",
            body=f"Tesla: 🔺{round(percent_dif)}%\n\n Headlines:{title}\n\n Read: {description}\n\n News By Daniel Jackson")
        print(message.status)

    elif 5 > percent_dif > 0:
        print(title)
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="+18556121826",
            to="+16466294880",
            body=f"Tesla: 🔻{round(percent_dif)} %\n Headlines:{title}\n Read:{description}"
                 f"\n\n News By Daniel Jackson")
        print(message.status)
