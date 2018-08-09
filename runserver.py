from flask import Flask
from flask import request
from flask import render_template

import os 
from dexterai import app, db

from config import DexterConfig

def main():
    HOST = 'https://dexter.azurewebsites.net' # os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = 80 # int(os.environ.get('SERVER_PORT', 80))
    except ValueError:
        PORT = 80

    app.run(HOST, PORT, debug=DexterConfig.DXTR_MODE)
 
if __name__ == '__main__':
    main()
