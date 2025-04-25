from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # aceita GET e POST
def home():
    if request.method == 'POST':
        nome = request.form.get('nome')
        qtd = request.form.get('qtd')
        return f'<h1>Material: {nome}, {qtd} unidades - recebido!</h1>'
    
    return render_template('index.html')  # se for GET, mostra o formulário

if __name__ == '__main__': 
    app.run(debug=True)

print('Servidor rodando...')
print('Caminho atual: ', os.getcwd())