# Welcome to TALE-Toolbox. Developed by Joshua Meier 
# in collaboration with with the Zhang Lab at MIT.
#
# To run this application yourself, please install its requirements first:
#
#   $ pip install -r sample_app/requirements.txt
#

from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

# do something with app...