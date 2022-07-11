from flask import Blueprint, flash, render_template, request, redirect, url_for

project = Blueprint('project', __name__, template_folder='project_templates')

@project.route('/weatherapp')
def weatherapp():
    return render_template('weatherapp.html')