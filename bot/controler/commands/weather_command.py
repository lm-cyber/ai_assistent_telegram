from .utils import date_convect
from bot.config import WEATHER_TOKEN
from bot.controler.user_context import UserData


class WeatherCommand:
    def __init__(self):
        pass

    def run(self, user_data: UserData, tokens: list[dict[str, str]]):
        date = date_convect(tokens[0]["word"])
        return {
            "user service": user_data.get_token("test"),
            "date in request": date,
            "token service": WEATHER_TOKEN,
        }
        # пример api много денек стоят
