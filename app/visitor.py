from flask import Blueprint,render_template, request, redirect
from .models import Article

visitor = Blueprint('visitor',__name__)

@visitor.route('/')
def index():
    return render_template('visitor/index.html')

@visitor.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404