from transformers import BertModel, BertTokenizer
from datasets import load_dataset
import pandas  as pd
import numpy as np


    model_path = "bert-base-uncased"
    tokenizer  = BertTokenizer.from_pretrained(model_path)
    dataset = load_dataset('osanseviero/twitter-airline-sentiment')
    dataset = dataset["train"].to_pandas()
    dataset = dataset[["airline_sentiment","text"]]
    dataset['airline_sentiment'] = dataset['airline_sentiment'].map({"positive" : 2, "negative" :1, "neutral" :0})
    x_train = dataset['text'].tolist()
    y_train = dataset['airline_sentiment'].tolist()
    y_train = np.array(y_train)
    tokenized_x_train = tokenizer(x_train,return_tensors='tf',padding =True)
    tokenized_x_train = dict(tokenized_x_train)
