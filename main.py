import os
import sys
import pandas as pd

sitepackage = "D:\home\site\wwwroot\env\Lib\site-packages"
sys.path.append(sitepackage)


from flask import Flask
app = Flask(__name__)
@app.route('/')

def test():
  
    # --------------test for checking Pandas ---------------- # 
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    df.head
    # ------------------------------------------------------- #

    return 'Python Flask works.'

if __name__ == '__main__':
    app.run()
