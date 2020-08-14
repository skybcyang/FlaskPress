from flask import Blueprint,render_template, request, redirect, session, url_for
from .models import Admin,Article
from app import form

admin = Blueprint('admin', __name__)

@admin.route('/')
def login():
    loginform = form.LoginForm()
    return render_template('/admin/login.html', loginform=loginform)

@admin.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404