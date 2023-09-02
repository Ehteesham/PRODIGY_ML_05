# Fruit Image Recognition and Calorie Prediction

## Summary

- This project uses a CNN model to detect fruits in images.
- It then scrapes calorie information for the detected fruits.
- I used tkinter to create a graphical user interface (GUI) where you can choose a fruit picture. Once you select a fruit picture, the program will predict the fruit and then use BeautifulSoup to scrape the web for information about the calories of that fruit.
- To make predictions, simply download this repository and run the following command:

  ```shell
  python app.py
  ```

## Dataset

If you prefer to train your own model, you can download the 'Fruit and Vegetable Image Recognition' dataset and follow these steps:

1. Click on this [link](https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition) to access the dataset on Kaggle.
2. Download the ZIP file containing the dataset.
3. Extract the contents of the ZIP folder and place them in the "DataSet" folder within this repository.
4. In the 'DataSet' folder, you will find a list of fruit names [View File](DataSet\fruits_classes.txt). This list represents the number of fruit classes used in the model.

## Folder Information

- **Jupyter Notebook (Notebook):** Contains notebooks related to model training and testing. You can access this folder using the following link: [View Folder](notebook).

- **Saved Model (model):** Contains the saved model responsible for fruit recognition. You can access this folder using the following link: [View Folder](model).

## Required Packages

To install the required packages, run the following command in the project's root directory:

```shell
pip install -r requirements.txt
```

Make sure you have Python installed on your system.
