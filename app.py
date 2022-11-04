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

@app.route("/report",)