from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField(label="Your Name", validators=[DataRequired()])
    email = StringField(label="Email I can reach you at", validators=[DataRequired()])
    message = TextAreaField(label="Message", validators = [DataRequired()])
    submit = SubmitField(label="Send")