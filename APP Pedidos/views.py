from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pedidos.html')
def pedidos():
    return render_template('pedidos.html')

