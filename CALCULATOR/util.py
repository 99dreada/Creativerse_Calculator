from flask import(
    request,
)
from functools import wraps
from CALCULATOR import app
from CALCULATOR.model import (
    db,
    Process_sql,
)
from CALCULATOR.forms import(
     Product_Form,
 )

@app.template_filter('dict_but')
def dict_but(d, **kwargs):
    return { **d, **kwargs }

def create_forms(*forms):
    def _inner(f):
        @wraps(f)
        def _wrapper(*args, **kwargs):
            def create_product_form(**kwargs):
                product_form = Product_Form(request.form)
                product_form.Process_id.choices = _choices_with_blank(Process_sql)
                return product_form
            mapping = {'product_form': create_product_form
                    }
            formObjs = {}
            for form in forms:
                formObjs[form] = mapping[form](**kwargs)
            return f(*args, forms=formObjs, **kwargs)
        return _wrapper
    return _inner

def _choices_with_blank(sql_obj):
    choices = db.session.query(sql_obj.id, sql_obj.Name).all()
    choices = [(0, '')] + choices # prepend blank
    return choices