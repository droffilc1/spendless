#!/usr/bin/python3
"""Blueprint for API"""
from flask import Blueprint

# Define Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.analytics import *
from api.v1.views.categories import *
from api.v1.views.expenses import *
from api.v1.views.index import *
from api.v1.views.login import *
from api.v1.views.register import *
