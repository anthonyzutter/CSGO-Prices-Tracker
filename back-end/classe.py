from config import *

class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    preco = db.Column(db.String(254))
    exterior = db.Column(db.String(254))
    quantidade = db.Column(db.String(254))

    def __str__(self):
        return str(self.id)+") " + self.nome + ", " +\
            self.preco + ", " + self.exterior + ", " +\
            self.quantidade

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "exterior": self.exterior,
            "quantidade": self.quantidade
        }