from flask import Blueprint, flash, render_template, request, redirect, url_for

landscape = Blueprint('landscape', __name__, template_folder='landscape_templates')

@landscape.route('/zurich-insurance-north-america')
def zna():
    return render_template('zna.html')

@landscape.route('/ministry-of-commerce-industry')
def mci():
    return render_template('mci.html')