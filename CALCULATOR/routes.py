from flask import(
    render_template,
    request,
)
from CALCULATOR import app
from CALCULATOR.util import(
    dict_but,
    create_forms,
)

@app.route('/', methods=['GET', 'POST'])
@create_forms('product_form')
def index(forms):
    if request.method == 'GET':
        pass
    elif form.validate_on_submit():
        print("worked")
    return render_template('index.html', **forms)

@app.route('/machines')
def machines():
    return render_template('machines.html')

@app.route('/materials')
def materials():
    return render_template('materials.html')

@app.route('/other')
def other():
    return render_template('other.html')