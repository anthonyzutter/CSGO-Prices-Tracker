from config import *
import os

class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=True)
    preco = db.Column(db.Float, nullable=True)
    preco_atual = db.Column(db.Float, nullable=True, default=0)
    data = db.Column(db.DateTime, nullable=True, default=datetime.today)

    def __str__(self):
        return f"Nome: {self.nome}, Preço compra: {self.preco}, Preço atual: {self.preco_atual}, Data: {self.data}"

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "preco_atual": self.preco_atual,
            "data": self.data
        }

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    i1 = Item(
        nome = "AK-47 | Redline (Field-Tested)", 
        preco = 82.62, 
        preco_atual = 0)

    i2 = Item(
        nome = "M4A4 | Desolate Space (Field-Tested)", 
        preco = 60.75, 
        preco_atual = 0)

    i3 = Item(
        nome = "AWP | Atheris (Minimal Wear)", 
        preco = 27.40, 
        preco_atual = 0)

    i4 = Item(
        nome = "Desert Eagle | Emerald Jörmungandr (Factory New)", 
        preco = 430.53, 
        preco_atual = 0)

    db.session.add(i1)
    db.session.add(i2)
    db.session.add(i3)
    db.session.add(i4)
    db.session.commit()

    print(i1)
    print(i1.json())
