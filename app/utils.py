from app import db
from app.models.pessoa import Pessoa
from app.models.usuario import Usuario


def inserir_pessoa(pessoa):
    db.session.add(pessoa)
    db.session.commit()
    return None


def listar_pessoas():
    pessoas = []
    try:
        consulta = Pessoa.query.all()
        for elemento in consulta:
            pessoas.append(elemento.retornar_pessoa())
        return pessoas

    except Exception as e:
        print(e)
    return None


def alterar_pessoa():
    db.session.commit()
    return None


def deletar_pessoa(id):
    pessoa = Pessoa.query.get_or_404(id)
    db.session.delete(pessoa)
    db.session.commit()
    return None


def valida_usuario():
    numero_usuario = len(Usuario.query.all())
    print(f"Número de Usuários: {numero_usuario}")
    if numero_usuario < 1:
        usuario = Usuario('admin', 'admin#2021')
        db.session.add(usuario)
        db.session.commit()
    return None

