import pandas as pd
from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
  data = np.array([['','Col1','Col2'], ['Row1',1,2], ['Row2',3,4]])              
  print(pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:]))
  
  return 'Hey its Python Flask application!'

if __name__ == '__main__':
  app.run()
