import Inference_pipeline.inference_scraping as inference_scraping
from transformers import TFBertForSequenceClassification

from transformers import pipeline


class ModelInference:

    def __init__(self):
        scraping_object = inference_scraping.Scrapping()
        self.data = scraping_object.get_tweets("United Airlines -is:retweet lang:en")
        self.model = model = TFBertForSequenceClassification.from_pretrained("../Model_training_pipeline/saved_model")
        # self.sentiment_pipeline = pipeline("sentiment-analysis")

    def get_inference(self):
        result = self.model(self.data)
        result_list = []
        for entry in result:
            result_list.append(entry['label'])
        count_positive = result_list.count('POSITIVE')
        count_negative = result_list.count('NEGATIVE')
        final_inference = {'POSITIVE' : count_positive , 'NEGATIVE' : count_negative }
        return final_inference

