from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # دریافت داده‌های فرم
    data = {
        'address': request.form.get('address'),
        'area': request.form.get('area'),
        'year': request.form.get('year'),
        'rooms': request.form.get('rooms'),
        'features': request.form.getlist('features')
    }
    
    # اینجا منطق پیش‌بینی قیمت را اضافه کنید
    # price = model.predict(data)
    
    return f"اطلاعات دریافت شد: {data}"

if __name__ == '__main__':
    app.run(debug=True)