from flask import Flask, render_template
import requests

print("building app")
app = Flask(__name__)

@app.route("/")
def home():
    print("getting")
    r = requests.get("https://loadshedding.eskom.co.za/LoadShedding/GetStatus").text
    print(r)
    return r

if __name__ == '__main__':
    app.run(debug=True)
