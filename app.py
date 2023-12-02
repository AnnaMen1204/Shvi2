import self as self
from flask import Flask, render_template, request
import pickle
import sklearn
from sklearn.linear_model import LinearRegression

from proceccing import get_message


app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def main():
    message = ''
    if request.method == 'POST':
        data = 'lr_modelshvi.pkl'
        with open('lr_modelshvi.pkl', 'wb') as f:
            pickle.dump(data, f)
        with open('lr_modelshvi.pkl', 'rb') as f:
            loaded_model = pickle.load(f)
            IW = float(request.form.get("IW"))
            IF = float(request.form.get("IF"))
            VW = float(request.form.get("VW"))
            FP = float(request.form.get("FP"))

        Width = [['IW', 'IF', 'VW', 'FP']]
        Depth = [['IW', 'IF', 'VW', 'FP']]
        message = f"Depth: {Depth}"
        message = f"Width: {Width}"
        message = get_message(Depth)
        message = get_message(Width)
        return render_template('index.html', message=message)


@app.route('/text')  # http://127.0.0.1:5000 + '/text' = http://127.0.0.1:5000/text
def text():
    return "Text"


