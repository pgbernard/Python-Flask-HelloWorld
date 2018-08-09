from flask import Flask
from flask import request
from flask import render_template

import pandas as pd
import numpy as np
import scipy
import sklearn

app = Flask(__name__)

@app.route("/")

def main():
	age = {"Variable": 10, "Variable2": 25, "Variable3": 33, "Variable4": 52}
	return render_template("index.html", ages = age)

if __name__ == "__main__":
    app.run()
