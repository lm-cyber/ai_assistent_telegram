from typing import Callable, Any
from .user_context import UserContext


class Controler:
    def __init__(self, user_context: UserContext):
        self.user_context = user_context
        self.callback: dict[Any, Callable] = {}
