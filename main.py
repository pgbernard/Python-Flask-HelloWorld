import os
import sys
import pandas as pd
import scipy as sp
import numpy as np

from flask import Flask
app = Flask(__name__)

def main():
    HOST = 'https://facebook-dexter-api-lnx.azurewebsites.net' # os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = 80 # int(os.environ.get('SERVER_PORT', 80))
    except ValueError:
        PORT = 80
    app.run(HOST, PORT, debug=DexterConfig.DXTR_MODE)
    
if __name__ == '__main__':
    main()

