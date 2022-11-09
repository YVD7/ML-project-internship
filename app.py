from flask import Flask, request
from flask_cors import cross_origin
import pickle

app = Flask(__name__)

model = pickle.load(open('Model.pkl','rb'))

@app.route("/",methods = ['GET','POST'])
@cross_origin()
def home():
    try:
        pass
    except Exception as e:
        raise e

@app.route("/predict",methods=["post"])
@cross_origin()
def predict():
    try:
        if request.method == "POST":
            try:
            #                 ['Cement (component 1)(kg in a m^3 mixture)',
            #  'Blast Furnace Slag (component 2)(kg in a m^3 mixture)',
            #  'Fly Ash (component 3)(kg in a m^3 mixture)',
            #  'Water  (component 4)(kg in a m^3 mixture)',
            #  'Superplasticizer (component 5)(kg in a m^3 mixture)',
            #  'Coarse Aggregate  (component 6)(kg in a m^3 mixture)',
            #  'Fine Aggregate (component 7)(kg in a m^3 mixture)',
            #  'Age (day)',
            #  'Concrete compressive strength(MPa, megapascals) ']
                  Cement (component 1)(kg in a m^3 mixture)

            except Exception as e:
                pass
    except Exception as e:
        pass