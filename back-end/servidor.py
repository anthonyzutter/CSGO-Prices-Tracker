from steam_community_market import Market
from config import app
from routes import *

market = Market("BRL")
game = 730

if __name__ == '__main__':
    itens = Item.query.get(1)
    #Pega o preço atual do item
    itens.preco_atual = market.get_lowest_price(itens.nome, game)
    db.session.commit()

    itens = Item.query.get(2)
    itens.preco_atual = market.get_lowest_price(itens.nome, game)
    db.session.commit()
    
    itens = Item.query.get(3)
    itens.preco_atual = market.get_lowest_price(itens.nome, game)
    db.session.commit()

    itens = Item.query.get(4)
    itens.preco_atual = market.get_lowest_price(itens.nome, game)
    db.session.commit()

    app.run(debug=True)
