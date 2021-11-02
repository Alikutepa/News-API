from flask import Blueprint
from flask.app import Flask
from flask_bootstrap import Blueprint
main = Blueprint('main', __name__)

from . import views,error

