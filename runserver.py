
from flask import Flask, flash, redirect, render_template, request, session, abort

import pandas as pd

app = Flask(__name__)

@app.route("/")

def hello():
    df_ = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
    number = 123456789
    return render_template('test.html', number=str(number), data = df_.to_html())

if __name__ == "__main__":
    app.run()
