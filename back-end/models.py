from config import *

class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=True)
    preco = db.Column(db.Float, nullable=True)
    preco_atual = db.Column(db.Float, nullable=True, default=0)
    url = db.Column(db.String(254), nullable=True, default="https://steamcommunity.com/market/listings/730/")
    data = db.Column(db.String(254), nullable=True, default=now.strftime("%d/%m/%Y"))

    def __str__(self):
        return f"Nome: {self.nome}, Preço compra: {self.preco}, Preço atual: {self.preco_atual}, Url: {self.url} Data: {self.data}"

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "preco_atual": self.preco_atual,
            "url": self.url,
            "data": self.data
        }

class Ranking(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.Integer, nullable=True)
    autor = db.Column(db.String(254), nullable=True)
    item_id = db.Column(db.Integer, db.ForeignKey(Item.id))
    item = db.relationship("Item")

    def __str__(self):
        return f"Nota: {self.nota}, Nome: {self.item}"

    def json(self):
        return {
            "id": self.id,
            "nota": self.nota,
            "autor": self.autor,
            "item_id": self.item_id,
            "item": self.item
        }

class Jogo(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=True)

    def __str__(self):
        return f"Nome: {self.nome}" 

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome
        }

#Criar item teste
if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    i1 = Item(
        nome = "AK-47 | Redline (Field-Tested)", 
        preco = 82.62)

    r1 = Ranking(nota = 8, autor = "James", item = i1)

    j1 = Jogo(nome = "Counter-Strike: Global Offensive")
    
    db.session.add(i1)

    db.session.add(r1)

    db.session.add(j1)

    db.session.commit()
    i1.url += i1.nome
    db.session.commit()
    print(i1)
    print(r1)
    print(j1)