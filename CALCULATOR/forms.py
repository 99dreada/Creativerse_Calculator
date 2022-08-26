from wtforms import (
    Form,
    IntegerField,
    SelectField,
    validators
)

from flask_wtf import FlaskForm
from CALCULATOR import app
from CALCULATOR.model import (
    Products_sql
)

class Product_Calculator(FlaskForm):
    model = Products_sql