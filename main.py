import pandas as pd
import numpy as np
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
    return 'ok 2'

def test():
    # Period for retrieving historical data = N previous days from today
    n_days = 30

    # Max Percentage of Keywords to remove
    # Number of the best interests keyword to subset to create separated adsets
    margin = .25
    top = 3

    # Get the START and END date for INSIGHTS DATA over 'n_days' ------------- # 

    #now = datetime.datetime.now()

    #year, month, day = now.year, now.month, now.day
    #period = now - datetime.timedelta(days = n_days)
    #year_p, month_p, day_p = period.year, period.month, period.day

    #end_dt = date(year, month, day)
    #start_dt = date(year_p, month_p, day_p)
    print(n_days / top)

#main()

if __name__ == '__main__':
    main()
