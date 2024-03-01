from config import REDIS_HOST, REDIS_PORT
from redis_dict import RedisDict

dic = RedisDict(host=REDIS_HOST, port=REDIS_PORT)


class UserData:
    def __init__(self, tokens_for_service: dict):
        self._tokens_for_service: dict = tokens_for_service

    def get_token(self, service_name: str):
        return self._tokens_for_service.get(service_name, None)


class UserContext:
    def __init__(self):
        self._storage = RedisDict(host=REDIS_HOST, port=REDIS_PORT)
        if "tokens" not in self._storage:
            self._storage["tokens"] = {}

    def set_tokens(self, user_id, name_service, token):
        if user_id not in self._storage["tokens"]:
            self._storage["tokens"][user_id] = {}
        self._storage["tokens"][user_id][name_service] = token

    def get_user_data_by_id(self, user_id) -> UserData:
        return UserData(self._storage["tokens"][user_id])
