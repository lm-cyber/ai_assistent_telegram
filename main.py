from ml.model import ModelNERNLU
from ml.controler import Controler
from ml.user_context import UserContext
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
import redis
from config import REDIS_HOST,REDIS_PORT
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
r.set('foo', 'bar')

print(r.get('foo'))
