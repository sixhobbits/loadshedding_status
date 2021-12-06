from flask import render_template
from app import app
import requests

app = Flask(__name__)

@app.route("/")
def home():
    print("getting")
    r = requests.get("https://loadshedding.eskom.co.za/LoadShedding/GetStatus").text
    print(r)
    return r
