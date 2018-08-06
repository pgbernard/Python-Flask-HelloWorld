import os
import sys
import pandas as pd
import numpy as np

from flask import Flask
app = Flask(__name__)

@app.route('/')

def test():
    # --------------test for checking Pandas ---------------- # 
    try:
        d = {'col1': [1, 2], 'col2': [3, 5]}
        df = pd.DataFrame(data=d)
        x = len(np.array([2,3,1,0]))
        #var = 'pandas is working'
    except:
        var = 'error'
    #print(df)
    # ------------------------------------------------------- #
    return x

if __name__ == '__main__':
    app.run()
