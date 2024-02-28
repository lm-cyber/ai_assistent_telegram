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


class ModelNERNLU:
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
        return self._NER(text)

    def get_all_tokens(self):
        return self._NER_labels
