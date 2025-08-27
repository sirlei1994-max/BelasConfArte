from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/bolos")
def bolos():
    return """
    <h2>🎂 Bolos</h2>
    <p><strong>Sabores:</strong> Chocolate, Cenoura, Fubá, Limão, Chantilly e mais!</p>
    <p><strong>Opções:</strong> Decorados, com recheio, personalizados com nome.</p>
    <p>Perfeitos para aniversários, festas e presentes.</p>
    <p><a href="/">← Voltar ao início</a></p>
    """

@app.route("/cestas")
def cestas():
    return """
    <h2>🧺 Cestas e Festa na Bandeja</h2>
    <p>Cestas decoradas com produtos artesanais, chocolates, flores e muito carinho.</p>
    <p>Perfeitas para presentear em aniversários, dia das mães, noivados, etc.</p>
    <p>Montamos com o tema que você escolher!</p>
    <p><a href="/">← Voltar ao início</a></p>
    """

@app.route("/kit-festa")
def kit_festa():
    return """
    <h2>🎁 Kit Festa</h2>
    <p>Montamos kits completos para tornar sua comemoração ainda mais fácil.</p>
    <p>Inclui:</p>
    <ul>
        <li>Docinhos personalizados</li>
        <li>Lembrancinhas</li>
        <li>Decoração temática</li>
        <li>Bandejas montadas</li>
    </ul>
    <p><a href="/">← Voltar ao início</a></p>
    """

@app.route("/todos")
def todos():
    return """
    <h2>📦 Tudo o que temos</h2>
    <p>Aqui você encontra todos os nossos produtos:</p>
    <ul>
        <li>🎂 Bolos artesanais</li>
        <li>🧺 Cestas decoradas</li>
        <li>🎁 Kit festa infantil e adulto</li>
        <li>🎀 Lembrancinhas personalizadas</li>
        <li>🎉 Festas na bandeja</li>
    </ul>
    <p><a href="/">← Voltar ao início</a></p>
    """

if __name__ == "__main__":
    app.run(debug=True)
