from flask import Blueprint, flash, render_template, request, redirect, url_for

project = Blueprint('project', __name__, template_folder='project_templates')

@project.route('/xxx')
def xxx():
    return render_template('xxx.html')

@project.route('/flash-cards-preview')
def flash_cards():
    return render_template('flash_cards.html')