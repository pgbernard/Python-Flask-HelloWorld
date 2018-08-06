import os
import sys
import pandas as pd
import scipy as sp
import numpy as np

from flask import Flask
app = Flask(__name__)

@app.route('/')

def test():
    arr = np.array([2,3,1,0])
    arrLength = len(arr)
    return arrLength
    #return len(np.array([2,3,1,0]))
    #d = {'col1': [1, 2], 'col2': [3, 5]}
    #df = pd.DataFrame(data=d)
    #return 'hello?'
    #x = len(np.array([2,3,1,0]))
    #return x

if __name__ == '__main__':
    app.run()
