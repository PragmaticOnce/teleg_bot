import sys
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header





def get_weather(url):
    # city = sys.argv[1]
    params = {'key': 'bc8574cffa64487c991132613202106',
              'q': 'Lviv',
              'format': 'json',
              'num_of_days': 1,
              'lang': 'ru'}
    r = requests.get(url, params=params)
    the_weather = r.json()
    if 'data' in the_weather:
        if 'current_condition' in the_weather['data']:
            try:
                return the_weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return 'Server Error'
    return 'Server Error'


def make_email(weather):
    text = "Weather in Lviv.\nTemperature: " + str(weather["temp_C"]) + " C\nFeels like: " + str(
        weather["FeelsLikeC"] + " C\nWind speed: " + str(weather["windspeedKmph"]) + "km/h")
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['Subject'] = Header("Погода у Львові.", 'utf-8')

    msg['From'] = "site@softtailor.ru"

    msg['To'] = "contact@softtailor.ru"
    return msg



def main():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    weather = get_weather(url)
    print(
        f'Температура повітря у Львові: {weather["temp_C"]}°C.\nВідчувається як: {weather["FeelsLikeC"]}°C.\nШвидкість вітру: {weather["windspeedKmph"]}km/h.')
    print(f'{weather["weatherIconUrl"]}')
    icon = requests.get(weather['weatherIconUrl'][0]['value'])
    with open("image.png", "wb") as image:
        image.write(icon.content)
    smtpObj.starttls()
    smtpObj.login('extlg.pragma@gmail.com', '#pragma_once')
    msg = "Weather in Lviv.\nTemperature: " + str(weather["temp_C"]) + " C\nFeels like: " + str(
        weather["FeelsLikeC"] + " C\nWind speed: " + str(weather["windspeedKmph"]) + "km/h")
    smtpObj.sendmail('extlg.pragma@gmail.com', 'pragmatic.once.lviv@gmail.com', make_email(weather).as_string())
    smtpObj.quit()


if __name__ == '__main__':
    main()