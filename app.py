import tensorflow as tf
from testing import FruitPrediction, FruitCaloriesPrediction
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import json


def read_params():
    with open("params.json", 'r') as params_file:
        params = json.load(params_file)
    return params


def get_size(params):
    height = params["img_params"]["img_height"]
    width = params["img_params"]["img_width"]
    return height, width


def open_image():
    params = read_params()
    fr_pred = FruitPrediction(params)
    img_height, img_width = get_size(params)
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if file_path:
        pred_name, pred_score = fr_pred.test_img(file_path)

        fr_calories = FruitCaloriesPrediction(pred_name)

        calories = fr_calories.get_calories()

        image = Image.open(file_path)
        img_resize = image.resize(
            (params["app_params"]["app_img_size"], params["app_params"]["app_img_size"]))
        img = ImageTk.PhotoImage(img_resize)
        label.config(image=img)
        label.image = img  # Keep a reference to the image to prevent garbage collection
        prediction_label.config(
            text=f"This is a {pred_name} with confidence score of {pred_score:.2f}")
        prediction_calories.config(text=f"Calories (100gm): {calories}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Viewer")

    # Get the screen width and height
    screen_width = 600
    screen_height = 500

    # Set the window dimensions to match the screen's width and height
    root.geometry(f"{screen_width}x{screen_height}")

    label = tk.Label(root)
    label.pack()

    open_button = tk.Button(root, text="Open Image", command=open_image)
    open_button.pack()

    # Create a label for displaying predictions
    prediction_label = tk.Label(root, text="", font=("Helvetica", 20))
    prediction_label.pack()

    prediction_calories = tk.Label(root, text="", font=("Helvetica", 20))
    prediction_calories.pack()

    root.mainloop()
