from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager


@login_manager.user_loader
def retorna_usuario(id_usuario):
    return Usuario.query.filter_by(id=id_usuario).first


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nickname = db.Column(db.String(64), unique=True)
    senha = db.Column(db.String(128))

    def __init__(self, nickname, senha):
        self.nickname = nickname
        self.senha = generate_password_hash(senha)

    def validacao_senha(self, senha_secreta):
        return check_password_hash(self.senha, senha_secreta)

