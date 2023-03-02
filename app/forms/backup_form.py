from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class BackupForm(FlaskForm):
    description = StringField('description', validators=[DataRequired()])
    source = StringField('source')
    target = StringField('target', validators=[DataRequired()])
    program = StringField('program', validators=[DataRequired()])
    options = StringField('options')
    frequency = SelectField(u'frequency', coerce=int)
