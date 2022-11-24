# this file will have bunch of routes inside 
# all route urls


# all of this routes are to be also included in __init__.py
from flask import Blueprint, render_template


views = Blueprint('views', __name__)

@views.route('/')
def home(): # can be any name
    return render_template('home.html')

