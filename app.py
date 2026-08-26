from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/interacao", methods=["GET", "POST"])
def interacao():

    resultado = None

    if request.method == "POST":

        nome = request.form["nome"]
        sobrenome = request.form["sobrenome"]
        idade = int(request.form["idade"])

        if idade >= 18:
            votar = "Você pode votar."
            dirigir = "Você pode dirigir."

        elif idade >= 16:
            votar = "Você pode votar."
            dirigir = "Você ainda não pode dirigir."

        else:
            votar = "Você ainda não pode votar."
            dirigir = "Você ainda não pode dirigir."

        resultado = {
            "nome": nome,
            "sobrenome": sobrenome,
            "idade": idade,
            "votar": votar,
            "dirigir": dirigir
        }

    return render_template("interacao.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
