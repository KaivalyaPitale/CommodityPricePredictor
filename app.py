# save this as app.py
from flask import Flask, escape, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        date = int(request.form['date'])
        month = int(request.form['month'])
        year = int(request.form['year'])

        prediction = model.predict([[
            year,month,date
        ]])

        return render_template("prediction.html", prediction_text="Predicted price {}".format(prediction))

    else:
        return render_template("prediction.html")


if __name__ == "__main__":
    app.run(debug=True)
