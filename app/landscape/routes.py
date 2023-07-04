from flask import Blueprint, flash, render_template, request, redirect, url_for

landscape = Blueprint('landscape', __name__, template_folder='landscape_templates')

@landscape.route('/zurich-insurance-north-america')
def zna():
    return render_template('zna.html')

@landscape.route('/ministry-of-commerce-industry')
def mci():
    return render_template('mci.html')

@landscape.route('/analog-media-lab')
def aml():
    return render_template('aml.html')

@landscape.route('/stewart-residence')
def stewart_residence():
    return render_template('stewart_residence.html')

@landscape.route('/streamside-residence')
def streamside_residence():
    return render_template('streamside_residence.html')

@landscape.route('/park-at-the-mart')
def park_at_the_mart():
    return render_template('park_at_the_mart.html')

@landscape.route('/lakeshore-east')
def lakeshore_east():
    return render_template('lakeshore_east.html')

@landscape.route('/raised-beds')
def raised_beds():
    return render_template('raised_beds.html')