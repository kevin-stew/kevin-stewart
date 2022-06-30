from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for

from config import Config
from app.forms import ContactForm

import smtplib
from email.message import EmailMessage


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

@site.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        # msg = EmailMessage()
        # msg.set_content(form.message.data)
        # msg['Subject'] = f"{form.name.data} | {form.email.data}"
        # msg['To'] = Config.MAIL_SENDTO
        # # msg['From'] = form.email.data

        # server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
        # server.starttls()  #function that 'starts' the server
        # server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
        # server.sendmail(Config.MAIL_USERNAME, Config.MAIL_SENDTO, msg.as_string())
        # server.quit()

        flash(f"Thanks for your message! I will get back to you as soon as I can :)")
        return render_template("index.html")

    return render_template("contact.html",form=form)