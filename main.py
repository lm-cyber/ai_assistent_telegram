from ml.model import ModelNERNLU

model = ModelNERNLU()
res = model.get_label("Какая будет погода в следующие выходные?")
print(res)

res = model.get_tokens("Какая будет погода в следующие выходные?")
print(res)
