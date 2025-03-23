# Tehran House Price Prediction

This project aims to predict house prices in Tehran using data collected from the Divar platform. The code processes raw housing data, performs exploratory data analysis (EDA) and visualization, pre-processes the data for modeling, tunes several regression models using GridSearchCV, and finally selects and saves the best performing model.

A [Google Colab version of this notebook](https://colab.research.google.com/drive/19QUVMy9dylD7fxBzKsK1jtoQCujWAmgg?usp=sharing) is also available.

---

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Preprocessing](#preprocessing)
- [Exploratory Data Analysis (EDA) and Visualization](#exploratory-data-analysis-eda-and-visualization)
- [Modeling and Hyperparameter Tuning](#modeling-and-hyperparameter-tuning)
  - [Models and Parameter Grids](#models-and-parameter-grids)
- [Model Evaluation and Selection](#model-evaluation-and-selection)
- [Saving the Best Model](#saving-the-best-model)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [License](#license)

---

## Overview

This project develops and compares multiple regression models to forecast house prices. The workflow includes:

1. **Data Cleaning:** Removing entries with non-numeric prices (e.g., "توافقی") and cleaning string data.
2. **Data Transformation:** Converting prices to numeric values, extracting location information from addresses, and converting categorical data (e.g., boolean flags) into numeric format.
3. **Feature Engineering:** Creating a new feature for price per square meter and combining several facility-related columns into one aggregate feature.
4. **Exploratory Data Analysis (EDA):** Visualizing the distribution of features such as room count, construction year, and house price statistics across different regions.
5. **Modeling:** Tuning various regression models (K-Nearest Neighbors, Decision Tree, Random Forest, Support Vector Regression, and Linear Regression) using GridSearchCV.
6. **Evaluation:** Comparing models based on training R², testing R², RMSE, and cross-validation accuracy using a radar chart.
7. **Model Saving:** Retraining the best model (based on combined criteria) and saving it along with the scaler for later use.

---

## Dataset

The dataset used is sourced from a housing price collection on the Divar platform. Each record contains information about:
- **Area:** Apartment area in square meters.
- **Construction:** Year of construction.
- **Room:** Number of rooms.
- **Warehouse, Parking, Elevator:** Boolean features indicating the presence of these facilities.
- **Address:** Location details.
- **Price:** Listed price in Tomans (raw string values which include the currency and formatting).

---

## Preprocessing

The data preprocessing steps include:

- **Removing Unpriced Homes:** Entries with non-numeric price labels (like "توافقی") are filtered out.
- **Price Cleaning:** The 'تومان' suffix and commas are removed, and prices are converted into integers.
- **Address Parsing:** Extracting the neighborhood/location by removing extra details such as time stamps.
- **Numeric Conversion:** Converting columns such as 'Construction', 'Area', and 'Room' from strings to integers and dropping invalid entries.
- **Boolean Standardization:** Converting facility-related columns to boolean then to integer (0 or 1).
- **Feature Engineering:** Calculating the house age (capped at 30 years) and creating an aggregate `facilities` score.
- **Encoding:** Using one-hot encoding for the 'Address' column to avoid misinterpreting categorical values.

---

## Exploratory Data Analysis (EDA) and Visualization

Key EDA steps include:
- Statistical summaries of features (e.g., average construction year, average area, and price ranges).
- Visualizations of feature distributions (e.g., pie charts for facility availability).
- Cross-tabulation and count plots for features like the number of rooms against facilities.
- Bar plots to compare mean prices across top and bottom locations.

These visualizations help to understand the data distribution and inform the modeling choices.

---

## Modeling and Hyperparameter Tuning

After preprocessing and scaling the data, the code performs hyperparameter tuning using GridSearchCV with 10-fold cross-validation for five different regression models.

### Models and Parameter Grids

Below is a summary table of the hyperparameters tuned for each model:

| Model                    | Hyperparameters Tuned                                                                                                                 |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **KNeighborsRegressor**  | - `n_neighbors`: [3, 5, 7, 9, 11]<br> - `weights`: ['uniform', 'distance']<br> - `p`: [1 (Manhattan), 2 (Euclidean)]         |
| **DecisionTreeRegressor**| - `max_depth`: [3, 5, 10, 20, None]<br> - `min_samples_split`: [2, 5, 10]<br> - `min_samples_leaf`: [1, 2, 4]<br> - `criterion`: ['squared_error', 'absolute_error'] |
| **RandomForestRegressor**| - `n_estimators`: [100, 200, 500]<br> - `max_depth`: [None, 10, 20, 30]<br> - `min_samples_split`: [2, 5]<br> - `min_samples_leaf`: [1, 2]<br> - `bootstrap`: [True, False] |
| **SVR**                  | - `kernel`: ['rbf', 'linear', 'poly']<br> - `C`: [0.1, 1, 10, 100]<br> - `gamma`: ['scale', 'auto']<br> - `epsilon`: [0.01, 0.1, 0.5] |
| **LinearRegression**     | - `fit_intercept`: [True, False]<br> - `positive`: [True, False]                                                                   |

The function `find_Parameters__` handles the grid search for each model, prints the best hyperparameters, and computes the performance metrics including training and testing R², RMSE, and cross-validated accuracy.

---

## Model Evaluation and Selection

The performance of each model is evaluated based on:
- **Training R²:** How well the model fits the training data.
- **Testing R²:** Generalization performance on unseen data.
- **RMSE:** Root Mean Squared Error for the predictions.
- **Cross-Validation Accuracy:** Mean R² from 10-fold CV.

A radar (tulip) chart visualizes the normalized metrics for easy comparison. A combined score (sum of normalized metrics) is used to determine the best performing model.

---

## Saving the Best Model

The best model is selected based on the combined score. In this example, the Linear Regression model (with specific hyperparameters) is retrained on the scaled training set and then saved as a pickle file along with the scaler. These files can be loaded later for prediction on new data.

---

## Dependencies

The project requires the following Python packages:
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- re (built-in)
- arabic_reshaper
- python-bidi
- pickle (built-in)

Install the necessary libraries (if not already installed) using pip:

```bash
pip install arabic_reshaper python-bidi
```

---

## Usage

1. **Clone or download the repository.**
2. **Upload the dataset:** Place the `housing-Raoofi.csv` file into the designated folder in your Google Drive.
3. **Run the notebook in Google Colab:** Open the notebook using the provided [Google Colab link](https://colab.research.google.com/drive/19QUVMy9dylD7fxBzKsK1jtoQCujWAmgg?usp=sharing).
4. **Follow the cell execution order:** The notebook cells execute from data loading and cleaning to model training, evaluation, and saving.
5. **Use the saved model for predictions:** The saved pickle files (`best_linear_model.pkl` and `scaler.pkl`) can be loaded in a separate script or notebook for inference.

---


