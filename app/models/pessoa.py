from app import db


class Pessoa(db.Model):
    __tablename__ = "pessoa"
    id_pessoa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    idade = db.Column(db.Integer, default=0)
    cargo = db.Column(db.String(64), nullable=True)
    congregacao = db.Column(db.String(64), nullable=True)

    def __init__(self, nome, sexo, idade, cargo, congreg):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.cargo = cargo
        self.congregacao = congreg

    def retornar_pessoa(self):
        dicionario_pessoa = {
            'id': self.id_pessoa,
            'nome': self.nome,
            'sexo': self.sexo,
            'idade': self.idade,
            'cargo': self.cargo,
            'congregacao': self.congregacao
        }

        return dicionario_pessoa

    def __repr__(self):
        return f"Nome: {self.nome} - Idade: {self.idade} - Sexo: {self.sexo}"
