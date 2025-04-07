import pickle
import pandas as pd

def load_model_and_predict(input_data):
    """
    Load saved model and make prediction on new data
    """
    try:
        # Load the trained model
        with open('model/best_model.pkl', 'rb') as file:
            model = pickle.load(file)


        # Load the scaler model
        with open('model/scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)

        # Use the loaded scaler
        input_data = scaler.transform(input_data)

            

        # Make prediction
        prediction = model.predict(input_data)
        return prediction[0]
    
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return None
