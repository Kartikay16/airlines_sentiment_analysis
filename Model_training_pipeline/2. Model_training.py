from transformers import TFBertForSequenceClassification
from Model_training_pipeline import Data_preprocessing
import tensorflow as tf


class ModelTraining:

    def train_model():
        training_data = Data_preprocessing.DataPreprocessing.get_data()
        tokenized_x_train = training_data(0)
        y_train = training_data(1)
        model = TFBertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)
        optimizer = tf.keras.optimizers.Adam(learning_rate=2e-5)
        loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
        model.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])
        train_ds = tf.data.Dataset.from_tensor_slices(
            ({'input_ids': tokenized_x_train}, y_train)
        ).shuffle(1000).batch(16)
        model.fit(train_ds, epochs=2)
        model.save('saved_model/')
