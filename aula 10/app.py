from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    strings = 'Página inicial'
    return render_template("index.html", string= strings)

@app.route('/cursos')
def cursos():
    lista_de_cursos = ['Desenvolvimento Web', 'POO', 'Python']
    return render_template("cursos.html", lista=lista_de_cursos)

@app.route('/cursos/<nome>')
def curso_nome(nome):
    if nome == 'devweb':
        habilidades = ['HTML', 'CSS', 'JavaScript']
        return render_template("info_curso.html", nome_curso = 'Desenvolvimento Web', habilidades = habilidades, dificuldade=2)
    elif nome == 'poo':
        habilidades = ['Dicionários', 'Tratamento de exceções', 'Classe',  'Herança']
        return render_template("info_curso.html", nome_curso='Programação Orientada a Objetos',  habilidades = habilidades, dificuldade=1)
    elif nome == 'python':
        return render_template("info_curso.html", nome_curso='Python')
    else:
        return "Curso inexistente"
    
if __name__ == '__main__':
    app.run(debug=True)