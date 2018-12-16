from flask import Flask, render_template
from servico.colorir_code import code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('originais/codigoFonte.html')

@app.route('/highlight')
def highlight():
    code()
    return render_template('alterados/codigoFinal.html')

if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)