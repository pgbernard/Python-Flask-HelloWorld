import os
import sys
import pandas as pd

from flask import Flask
app = Flask(__name__)
@app.route('/')

def test():
  
    # --------------test for checking Pandas ---------------- # 
    d = {'col1': [1, 2], 'col2': [3, 5]}
    df = pd.DataFrame(data=d)
    #print(df)
    # ------------------------------------------------------- #
    var = len(df)
    return var

if __name__ == '__main__':
    app.run()
