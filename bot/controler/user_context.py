from redis_dict import RedisDict
from bot.config import REDIS_HOST, REDIS_PORT

dic = RedisDict(host=REDIS_HOST, port=REDIS_PORT)


class UserData:
    def __init__(self, tokens_for_service: dict):
        self._tokens_for_service: dict = tokens_for_service

    def get_token(self, service_name: str):
        return self._tokens_for_service.get(service_name, None)

    def __repr__(self):
        return str(self._tokens_for_service)


class UserContext:
    def __init__(self):
        self._storage: RedisDict = RedisDict(host=REDIS_HOST, port=REDIS_PORT)
        if "tokens" not in self._storage:
            self._storage["tokens"] = dict()

    def set_tokens(self, user_id, name_service, token):
        # будет очень медленный метод
        if user_id not in self._storage["tokens"]:
            t = dict()
            dict_temp = self._storage["tokens"]  # баги в либе, поэтому так
            dict_temp.update({user_id: dict()})
            self._storage["tokens"] = dict_temp
        dict_temp = self._storage["tokens"]  # баги в либе, поэтому так
        dict_temp[user_id].update({name_service: token})
        self._storage["tokens"] = dict_temp

    def get_user_data_by_id(self, user_id) -> UserData:
        return UserData(self._storage["tokens"][user_id])
