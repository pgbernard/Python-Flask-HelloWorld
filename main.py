
import os
import sys

sitepackage = "D:\home\site\wwwroot\env\Lib\site-packages"
sys.path.append(sitepackage)

import pandas as pd

from flask import Flask
app = Flask(__name__)
# --------------------------------------------------------- #

@app.route('/')


def hello_world():
  
  # --------------test for checking Pandas ---------------- # 
  d = {'col1': [1, 2], 'col2': [3, 4]}
  df = pd.DataFrame(data=d)
  df
  #a = np.array([1, 2, 3])
  #print(a)
  # ------------------------------------------------------- #
  
  return 'Hey its Python Flask application!'

if __name__ == '__main__':
  app.run()
