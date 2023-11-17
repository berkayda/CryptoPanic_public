import requests
import json
import time

api_key = "YOURAPIKEY"

response = requests.get(f"https://cryptopanic.com/api/v1/posts/?auth_token={api_key}")
news = response.json()

lastTitle = news['results'][0]['title']
lastURL = news['results'][0]['url']

def telegram_bot_sendtext(bot_mesaj, id: str):
    bot_token = 'YOURTELEGRAMBOTTOKEN'
    bot_chatID = id
    telegramURL = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(
        bot_chatID) + '&parse_mode=Markdown&text=' + bot_mesaj
    responseTelegram = requests.get(telegramURL)

if response.status_code == 200:
    print(lastTitle)
    print(lastURL)
    print("----------------------------------------------------------------------------------------------------")
    telegram_bot_sendtext(lastTitle + " " + lastURL, '@CryptocurrencyNewsBlog')

    while True:
        response = requests.get(f"https://cryptopanic.com/api/v1/posts/?auth_token={api_key}")
        news = response.json()

        if news['results'][0]['title'] != lastTitle and news['results'][0]['url'] != lastURL:
            telegram_bot_sendtext(news['results'][0]['title'] + " " + news['results'][0]['url'], '@CryptocurrencyNewsBlog')
            print(news['results'][0]['title'])
            print(news['results'][0]['url'])
            print("----------------------------------------------------------------------------------------------------")
            lastTitle = news['results'][0]['title']
            lastURL = news['results'][0]['url']

        time.sleep(60)

else:
    print("ERROR: ", response.status_code)
    print("ERROR MESSAGE: ", response.text)
