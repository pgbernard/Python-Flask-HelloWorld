print('try to import os, sys')
import os
import sys

# --------------------------------------------------------- #

try:
  print('try to import pandas')
  import pandas as pd
  from flask import Flask
  app = Flask(__name__)

except error:
  print(error)

@app.route('/')

def hello_world():
  
  # --------------test for checking Pandas ---------------- # 
  d = {'col1': [1, 2], 'col2': [3, 4]}
  df = pd.DataFrame(data=d)
  df
  # ------------------------------------------------------- #
  
  return 'Hey its Python Flask application!'

if __name__ == '__main__':
  app.run()
