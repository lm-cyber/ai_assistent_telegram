# from ml.model import ModelNERNLU
# from ml.controler import Controler
# from ml.user_context import UserContext
#
# model = ModelNERNLU()
#
# control = Controler(UserContext(), model)
# print(control.run("id user", "Какая будет погода в следующие выходные?"))
#
# res = model.get_label("Какая будет погода в следующие выходные?")
# print(res)
#
# res = model.get_tokens("Какая будет погода в следующие выходные?")
# print(res)
#
#
# res = model.get_tokens(
#     """Члены Американской академии киноискусств решили присудить режиссеру Дэвиду Линчу почетную премию "Оскар" за выдающийся вклад в кинематограф, сообщается на сайте академии. Церемония награждения пройдет 27 октября в развлекательном комплексе Hollywood and Highland Center в Лос-Анджелесе (штат Калифорния, США)."""
# )
# print(res)
from config import REDIS_HOST, REDIS_PORT
from redis_dict import RedisDict

dic = RedisDict(host=REDIS_HOST, port=REDIS_PORT)
# dic['foo'] = 42
# print(dic['foo'])  # Output: 42
# print('foo' in dic)  # Output: True
# dic["baz"] = "hello world"
# print(dic)  # Output: {'foo': 42, 'baz': 'hello world'}
#
# dic['test']={
#     'tokens':
#         {
#             "userid1":
#              {
#                  "serves1":"ttt",
#                  "serves2": "ttt2",
#              }
#         }
# }
print(dic)
