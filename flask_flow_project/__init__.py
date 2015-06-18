print('inner __init__.py')

from flask import Flask
app = Flask(__name__)
from flask_flow_project import views
