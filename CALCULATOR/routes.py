from flask import(
    render_template,
)
from CALCULATOR import app
"""from CALCULATOR.util import (
    retrieve_data,
)"""
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/machines')
def machines():
    return render_template('machines.html')

@app.route('/materials')
def materials():
    return render_template('materials.html')

@app.route('/other')
def other():
    return render_template('other.html')