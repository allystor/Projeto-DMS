from disputa import Adcionando
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar')
def adicionar():
    return render_template('adicionar_times.html')

if __name__ == '__main__':
    app.run(debug=True)