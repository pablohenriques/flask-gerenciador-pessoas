from flask import request, redirect, render_template, make_response

from app import app
from app import utils as database
from app.models.pessoa import Pessoa
from app.models.usuario import Usuario
from flask_login import login_user, logout_user


@app.route("/")
def initial():
    return render_template("initial.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        dados = {"nickname": request.form["nickname"], "senha": request.form["senha"]}

        try:
            usuario = Usuario.query.filter_by(nickname=dados["nickname"]).first()
            login_user(usuario)
            return redirect("/home")
        except Exception as e:
            print(e)
    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/cadastro_pessoa", methods=["GET", "POST"])
def cadastrar_pessoa():
    if request.method == "GET":
        return render_template("cadastro-pessoa.html")

    requisicao = request.form
    dados = {
        'nome': requisicao.get("nome_pessoa"),
        'sexo': requisicao.get("sexo_pessoa"),
        'idade': requisicao.get("idade_pessoa"),
        'cargo': requisicao.get("cargo_pessoa"),
        'congreg': requisicao.get("congregacao_pessoa")
    }

    nova_pessoa = Pessoa(**dados)
    try:
        database.inserir_pessoa(nova_pessoa)
    except Exception as e:
        print(e)
        return make_response({'mensagem': 'Erro Interno'}, 500)
    return redirect("/home")


@app.route("/listar_pessoas", methods=['GET'])
def listar_pessoas():
    lista_de_pessoas = database.listar_pessoas()
    return render_template('lista-pessoas.html', lista_pessoas=lista_de_pessoas)


@app.route("/alterar_pessoa/<int:id>", methods=['GET', 'POST'])
def alterar_pessoa(id):
    pessoa = Pessoa.query.get_or_404(id)
    print(f"Pessoa: {pessoa}")

    if request.method == "POST":
        requisicao = request.form
        dados = {
            'nome': requisicao.get("nome_pessoa"),
            'sexo': requisicao.get("sexo_pessoa"),
            'idade': requisicao.get("idade_pessoa"),
            'cargo': requisicao.get("cargo_pessoa"),
            'congreg': requisicao.get("congregacao_pessoa")
        }
        pessoa.nome = dados['nome']
        pessoa.sexo = dados['sexo']
        pessoa.idade = dados['idade']
        pessoa.cargo = dados['cargo']
        pessoa.congregacao = dados['congreg']
        print(f"Pessoa: {pessoa}")

        try:
            database.alterar_pessoa()
        except Exception as e:
            print(e)
        return redirect("/listar_pessoas")

    return render_template("altera-pessoa.html", pessoa=pessoa)


@app.route("/deletar_pessoa/<int:id>")
def deletar_pessoa(id):
    try:
        database.deletar_pessoa(id)
    except Exception as e:
        print(e)

    return redirect("/listar_pessoas")
