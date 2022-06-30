from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators, ValidationError
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField(label="Your Name", validators=[DataRequired()])
    email = StringField(label="Email I can reach you at", validators=[DataRequired(), validators.Email()])
    message = TextAreaField(label="Message", validators = [DataRequired()])
    submit = SubmitField(label="Send")