from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/sobre-mi')
def sobre_mi():
    return render_template('sobre_mi.html')

if __name__ == '__main__':
    app.run(debug=True)