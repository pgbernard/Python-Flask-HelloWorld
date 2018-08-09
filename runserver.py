from flask import Flask, render_template

import pandas as pd

app = Flask(__name__)

@app.route("/")

def hello():
    age = {"Sam": 20, "Ken": 30, "Grace": 23, "Peter": 29}
    return render_template("test.html", ages=age)

if __name__ == "__main__":
    app.run()
