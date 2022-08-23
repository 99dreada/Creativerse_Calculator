from flask import(
    render_template,
)
from CALCULATOR import app

@app.route('/')
def index():
    return render_template('index.html')