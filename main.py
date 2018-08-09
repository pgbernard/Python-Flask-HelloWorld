#import pandas as pd
#import numpy as np
#import json
#import datetime
#import time
#import math
                                                                                                            
#from sklearn.preprocessing import MinMaxScaler
#from sklearn.preprocessing import minmax_scale
#from sklearn import preprocessing
#from datetime import timedelta, date

from flask import Flask
app = Flask(__name__)

@app.route('/')

def main():
    return 'ok'


if __name__ == '__main__': 
    main()
