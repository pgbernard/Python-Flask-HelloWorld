from flask import Flask
from flask import request
from flask import render_template

import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")

def main():
	age = {"Sam": 20, "Ken": 30, "Grace": 23, "Peter": 29}
	return render_template("index.html", ages = age)

if __name__ == "__main__":
    app.run()
