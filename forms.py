from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import Optional, URL, AnyOf, NumberRange

class PetAddForm(FlaskForm):
    """Pet adding form"""
    name = StringField('Name')
    species = StringField('Species', validators=[AnyOf(values=['cat','dog','porcupine'])])
    img_url = StringField('Image URL', validators=[Optional(), URL(require_tld=False)])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30)])
    notes = StringField('Notes')

class PetEditForm(FlaskForm):
    """Pet editing form"""
    img_url = StringField('Image URL', validators=[Optional(), URL(require_tld=False)])
    notes = StringField('Notes')
    available = BooleanField('Availability')

