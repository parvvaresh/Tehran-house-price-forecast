import pandas as pd
from utils import load_model_and_predict
from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

def currency_format(value):
    return "{:,.0f}".format(value).replace(",", ",")

app.jinja_env.filters['currency_format'] = currency_format

# لیست کامل آدرس‌ها (مطابق با لیست اولیه)
with open("data/address.json", "r") as file:
    ALL_ADDRESSES = json.load(file)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = {
            'address': request.form.get('address'),
            'area': float(request.form.get('area')),
            'year': int(request.form.get('year')),
            'rooms': int(request.form.get('rooms')),
            'features': request.form.getlist('features')
        }

        if not data['address'] or data['address'] not in ALL_ADDRESSES:
            raise ValueError("آدرس انتخاب شده معتبر نیست")

        if not (20 <= data['area'] <= 500):
            raise ValueError("متراژ باید بین ۲۰ تا ۵۰۰ متر باشد")

        if not (1320 <= data['year'] <= 1403):
            raise ValueError("سال ساخت باید بین ۱۳۲۰ تا ۱۴۰۳ باشد")

        address_dict = {f'Address_{addr}': 0 for addr in ALL_ADDRESSES}
        address_dict[f'Address_{data["address"]}'] = 1

        current_year = 1403
        building_age = min(current_year - data['year'], 30)

        amenities_sum = sum([
            1 if 'انبار' in data['features'] else 0,
            1 if 'پارکینگ' in data['features'] else 0,
            1 if 'آسانسور' in data['features'] else 0
        ])

        df = pd.DataFrame([{
            'Area': data['area'],
            'Building_Age': building_age,
            'Rooms': data['rooms'],
            'Amenities_Sum': amenities_sum,
            **address_dict
        }])

        prediction = load_model_and_predict(df)
        
        return redirect(url_for('show_result', prediction=prediction))

    except Exception as e:
        return render_template('error.html', error_message=str(e))




@app.route('/result')
def show_result():
    prediction = request.args.get('prediction', '')
    try:
        return render_template('result.html', prediction=float(prediction) * 3)
    except:
        return render_template('error.html', error_message="مشکل در نمایش نتایج")


if __name__ == '__main__':
    app.run(debug=True, port=5002)