from flask import Flask, request, render_template
from livro import filtrar_livros
from bd import livros_disponiveis

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = []
    criterios_filtro = {}

    if request.method == "POST":
        # Recolhe os critérios preenchidos no formulário
        autor = request.form.get("autor")
        genero = request.form.get("genero")
        titulo = request.form.get("titulo")

        if autor: # permite filtrar apenas por autor, apenas por gênero, apenas por título ou por todos os campos.
            criterios_filtro["autor"] = autor
        if genero:
            criterios_filtro["genero"] = genero
        if titulo:
            criterios_filtro["titulo"] = titulo


        # Filtro
        resultados = filtrar_livros(livros=livros_disponiveis, criterios=criterios_filtro)

    return render_template("index.html", resultados=resultados)

if __name__ == "__main__":
    app.run(debug=True)