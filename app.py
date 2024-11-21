import os
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_number():
    numero = int(request.form['numero'])
    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
