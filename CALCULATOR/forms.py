from wtforms import (
    StringField,
    SelectField,
    validators
)
from CALCULATOR import app
from wtforms_alchemy import (
    ModelForm,
    QuerySelectField,
)
from CALCULATOR.model import (
    Products_sql,
    Process_sql
)

RELATIONVALSKW = {
    'validators': [
        validators.InputRequired(),
        validators.NoneOf([0], message="Please select one"),
    ],
    'coerce': int,
}

class Product_Form(ModelForm):
     class Meta:
         model = Products_sql
     Process_id = SelectField('Process_id', **RELATIONVALSKW)
