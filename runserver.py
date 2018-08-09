from flask import Flask

import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")

def main():
    age = {"Sam": 20, "Ken": 30, "Grace": 23, "Peter": 29}
    return ("index.html")

if __name__ == "__main__":
    app.run()
