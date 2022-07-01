from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/about')
def about():
    return render_template('about.html')

@site.route('/projects')
def projects():
    return render_template('projects.html')

@site.route('/contact')
def contact():
    return render_template('contact.html')