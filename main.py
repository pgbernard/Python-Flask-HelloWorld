import os
import sys
import pandas as pd
import scipy as sp
import numpy as np

from flask import Flask
app = Flask(__name__)

@app.route('/')

def main():
    return 'ok'

if __name__ == '__main__':
    main()
