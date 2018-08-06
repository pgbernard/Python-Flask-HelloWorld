import os
import sys
from flask import Flask
app = Flask(__name__)

# --------------------------------------------------------- #

try:
  import pandas as pd
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
