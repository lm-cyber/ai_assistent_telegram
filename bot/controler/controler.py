from typing import Callable, Any
from . import UserContext
from .commands import WeatherCommand
from bot.ml.model import ModelNERNLU


class Controler:
    def __init__(self, user_context: UserContext, model: ModelNERNLU):
        self._user_context = user_context
        self._command: dict[str, Any] = {"weather_query": WeatherCommand()}
        self.model = model

    def run(self, user_id, text):
        user_data = self._user_context.get_user_data_by_id(user_id)
        label = self.model.get_label(text)[0]["label"]
        tokens = self.model.get_tokens(text)
        return self._command[label].run(user_data, tokens)
