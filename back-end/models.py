from config import *
import os

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

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    i1 = Item(
        nome = "AK-47 | Redline (Field-Tested)", 
        preco = "R$ 82,62", 
        exterior = "Testada em Campo", 
        quantidade = "3")

    i2 = Item(
        nome = "M4A4 | Desolate Space (Field-Tested)", 
        preco = "R$ 60,75", 
        exterior = "Testada em Campo", 
        quantidade = "2"
        )

    i3 = Item(
        nome = "AWP | Atheris (Minimal Wear)", 
        preco = "R$ 27,40", 
        exterior = "Pouco Usada", 
        quantidade = "1")

    i4 = Item(
        nome = "Desert Eagle | Emerald Jörmungandr (Factory New)", 
        preco = "R$ 430,53", 
        exterior = "Nova de Fábrica", 
        quantidade = "1")

    db.session.add(i1)
    db.session.add(i2)
    db.session.add(i3)
    db.session.add(i4)
    db.session.commit()

    print(i1)
    print(i1.json())

    #print(i2.json())
    #print(i3.json())
    #print(i4.json())