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

#Criar item teste
if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    i1 = Item(
        nome = "AK-47 | Redline (Field-Tested)", 
        preco = 82.62)
    
    db.session.add(i1)
    db.session.commit()
    i1.url += i1.nome
    db.session.commit()
    print(i1)
