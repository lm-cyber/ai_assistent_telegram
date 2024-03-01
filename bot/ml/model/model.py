from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TextClassificationPipeline,
    AutoModelForTokenClassification,
    TokenClassificationPipeline,
)
from .config_model import (
    NER_labels,
    NLU_labels,
)
import re


class ModelNERNLU:
    @staticmethod
    def convector_tokens_classifier(tokens_list):
        tokens_concat = []
        num_before = -1
        for i in tokens_list:
            entity = re.sub(r".+-", "", i["entity"])
            if len(tokens_concat) != 0 and (
                (num_before + 1) == i["start"] and entity == tokens_concat[-1]["entity"]
            ):  # думать лень спать хочу
                tokens_concat[-1]["word"] += i["word"].replace("▁", " ")

            elif len(tokens_concat) == 0 or num_before < i["start"]:
                tokens_concat.append(
                    {
                        "entity": entity,
                        "word": i["word"].replace("▁", " "),
                    }
                )
            else:
                tokens_concat[-1]["word"] += i["word"].replace("▁", " ")
            num_before = i["end"]
        return tokens_concat

    def __init__(self):
        NLU_name = "qanastek/XLMRoberta-Alexa-Intents-Classification"
        tokenizer_NLU = AutoTokenizer.from_pretrained(NLU_name)
        model_NLU = AutoModelForSequenceClassification.from_pretrained(NLU_name)
        self._NLU = TextClassificationPipeline(model=model_NLU, tokenizer=tokenizer_NLU)

        NER_name = "qanastek/XLMRoberta-Alexa-Intents-NER-NLU"
        tokenizer_NER = AutoTokenizer.from_pretrained(NER_name)
        model_NER = AutoModelForTokenClassification.from_pretrained(NER_name)
        self._NER = TokenClassificationPipeline(
            model=model_NER, tokenizer=tokenizer_NER
        )

        self._NER_labels = NER_labels
        self._NLU_labels = NLU_labels

    def get_label(self, text):
        return self._NLU(text)

    def get_all_labels(self):
        return self._NLU_labels

    def get_tokens(self, text):
        return ModelNERNLU.convector_tokens_classifier(self._NER(text))

    def get_all_tokens(self):
        return self._NER_labels
