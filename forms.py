from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Pass', validators=[DataRequired()])
    submit = SubmitField('Submit')
