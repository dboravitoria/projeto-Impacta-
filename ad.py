from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<name>')
def curso_name(name):
    if name == 'index.html':
        return render_template("index.html")
    elif name == 'disciplinas.html':
        return render_template("disciplinas.html")
    elif name == 'contato.html':
        return render_template("contato.html")
    else:
        return render_template("error.html")
    
if __name__ == '__main__':
    app.run(debug=True)