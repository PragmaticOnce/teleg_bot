from cfg import _BOT_TOKEN, _WEATHER_URL
import telebot
import weather

bot = telebot.TeleBot(_BOT_TOKEN)
print(weather.get_weather(_WEATHER_URL))
kb = telebot.types.ReplyKeyboardMarkup(True, True)
kb.row('Сам поешь.', 'Ты быканул или мне показалось?')


def make_weather_msg(weather_status):
    text = "Weather in Lviv.\nTemperature: " + str(weather_status["temp_C"]) + " C\nFeels like: " + str(
        weather_status["FeelsLikeC"] + " C\nWind speed: " + str(weather_status["windspeedKmph"]) + "km/h")
    return text
@bot.message_handler(commands=['start'])
def setup(msg):
    bot.send_message(msg.chat.id, 'Hello', reply_markup=kb)
    user_id = msg.chat.id
    bot.send_sticker(user_id, 'CAACAgIAAxkBAAMyXvNlTc-HyIeRs6UBiW469brRik8AAp8BAAJl_5IKNOOPLcCcTG0aBA')

@bot.message_handler(content_types=['text'])
def text_message(msg):
    user_id = msg.chat.id
    message = msg.text
    print(message)
    if message == 'Погода':
        bot.send_message(user_id, make_weather_msg(weather.get_weather(_WEATHER_URL)))
        photo = open('image.png', 'rb')
        bot.send_photo(user_id, photo)
    if user_id == 623390631:
        bot.send_message(user_id, "Hello my creator!!!" )



@bot.message_handler(content_types=['sticker'])
def sticker_message(msg):
    print(msg)

bot.polling(none_stop=True)
