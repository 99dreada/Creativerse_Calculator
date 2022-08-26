from wtforms import (
    StringField,
)
from CALCULATOR import app
from wtforms_alchemy import ModelForm
from CALCULATOR.model import (
    Products_sql
)

class Product_Calculator(ModelForm):
    class Meta:
        model = Products_sql
