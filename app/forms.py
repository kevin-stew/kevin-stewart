from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField

from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField(label="Your Name:", validators=[DataRequired("I need to know your name.")])
    email = EmailField(label="Email I can reach you at:", validators=[DataRequired(), Email()])
    message = TextAreaField(label="Message:", validators = [DataRequired()])
    submit = SubmitField(label="Send")