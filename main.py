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
    arrLen = len(arr)
    return 'It is all good with using numpy'

if __name__ == '__main__':
    app.run()
