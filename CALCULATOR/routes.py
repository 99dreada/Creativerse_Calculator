from flask import(
    render_template,
    request,
)
from CALCULATOR import app
"""from CALCULATOR.util import (
    retrieve_data,
)"""
from CALCULATOR.forms import Product_Calculator

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Product_Calculator()
    if request.method == 'GET':
        pass
    elif form.validate_on_submit():
        print("worked")
    return render_template('index.html',form=form)

@app.route('/machines')
def machines():
    return render_template('machines.html')

@app.route('/materials')
def materials():
    return render_template('materials.html')

@app.route('/other')
def other():
    return render_template('other.html')