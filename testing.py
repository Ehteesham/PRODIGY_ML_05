import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup


class FruitPrediction:
    def __init__(self, params):
        self.params = params
        self.img_height = self.params["img_params"]["img_height"]
        self.img_width = self.params["img_params"]["img_width"]
        self.model_dir = self.params["dir"]["model_path"]
        self.class_name = os.listdir(self.params["dir"]["train_dataset"])

    def test_img(self, img_dir):
        model = load_model(self.model_dir)
        img = tf.keras.utils.load_img(
            img_dir, target_size=(self.img_height, self.img_width)
        )
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create a batch

        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        return self.class_name[np.argmax(score)], 100 * np.max(score)


class FruitCaloriesPrediction:
    def __init__(self, pred_name):
        self.pred_name = pred_name

    def get_calories(self):
        url = "https://www.google.com/search?q=calories+in" + self.pred_name
        req = requests.get(url).text
        soup = BeautifulSoup(req, 'html.parser')
        calories = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
        return calories
