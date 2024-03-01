from bot.ml.model import ModelNERNLU
from bot.controler import Controler
from bot.controler.user_context import UserContext

model = ModelNERNLU()

user_con = UserContext()
user_con.set_tokens("user_id_test", "test", "test_token")
# print(user_con.get_user_data_by_id("user_id_test"))
contol = Controler(user_context=user_con, model=model)
print(contol.run("user_id_test", "What will the weather be like tomorrow?"))
