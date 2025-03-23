# Tehran House Price Prediction Web App

This repository contains a web application for predicting house prices in Tehran based on features such as area, construction year, room count, amenities, and location. The model was developed using machine learning techniques and deployed as a Flask web app.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [License](#license)

## Overview

The application processes user inputs for a given property (e.g., area, year built, number of rooms, and available amenities) along with the location. It then predicts the house price using a pre-trained Linear Regression model. The model and the scaler are stored as pickle files in the `model` folder. The application also provides basic error handling and input validation.

A [Google Colab version of the notebook](https://colab.research.google.com/drive/19QUVMy9dylD7fxBzKsK1jtoQCujWAmgg?usp=sharing) used to develop the model is available.

## Features

- **User-Friendly Web Interface:** Allows users to enter property details through a simple HTML form.
- **Input Validation:** Validates inputs such as area (20–500 m²) and construction year (1320–1403).
- **Model Prediction:** Uses a saved Linear Regression model to generate price predictions.
- **Result Display:** Predicted prices are formatted using a custom currency filter.
- **Error Handling:** Displays appropriate error messages for invalid input or system issues.

## Repository Structure

```
├── app.py                      # Flask application file for running the web app.
├── model
│   ├── best_linear_model.pkl   # Pickled trained Linear Regression model.
│   ├── README.md               # README specific to the model folder.
│   └── scaler.pkl              # Pickled StandardScaler used for model input normalization.
├── __pycache__
│   └── utils.cpython-312.pyc   # Cached bytecode for the utils module.
├── static                      # Contains static files (CSS, JavaScript, images).
│   ├── icon.jpg
│   ├── script.js
│   └── styles.css
├── templates                   # HTML templates for rendering the web pages.
│   ├── error.html
│   ├── index.html
│   └── result.html
└── utils.py                    # Utility functions including model loading and prediction.
```

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/parvvaresh/Tehran-house-price-forecast
   cd Tehran-house-price-forecast
   ```

2. **Create a Virtual Environment (Optional):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   Make sure you have Flask and other required libraries installed:
   ```bash
   pip install -r requirements.txt
   ```


4. **Model Files:**
   Ensure that the model files (`best_linear_model.pkl` and `scaler.pkl`) are present in the `model` directory.

## Usage

1. **Run the Flask Application:**
   ```bash
   python app.py
   ```
   The app will start on port 5002 (or the specified port).

2. **Access the Web Interface:**
   Open your web browser and navigate to `http://127.0.0.1:5002/`.

3. **Input Data:**
   - Choose a valid address from the provided list.
   - Enter property area (between 20 and 500 square meters).
   - Input the year of construction (between 1320 and 1403).
   - Select the number of rooms.
   - Choose available amenities (e.g., انبار, پارکینگ, آسانسور).

4. **View Prediction:**
   Once the form is submitted, the application will redirect to a results page showing the predicted price.

## File Descriptions

- **app.py:** Main Flask application that defines routes, handles user input, performs prediction using the model, and renders templates.
- **utils.py:** Contains helper functions, including `load_model_and_predict`, which loads the pickled model and scaler to perform predictions.
- **model/**: Contains the trained model (`best_linear_model.pkl`) and scaler (`scaler.pkl`), along with a README specific to the model.
- **templates/:**
  - **index.html:** Home page with the input form.
  - **result.html:** Displays the predicted price.
  - **error.html:** Shows error messages for invalid inputs or system errors.
- **static/:**
  - **styles.css:** Styling for the web app.
  - **script.js:** JavaScript code for any dynamic functionality.
  - **icon.jpg:** Icon or image used in the application.

