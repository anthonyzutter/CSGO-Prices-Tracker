from steam_community_market import Market
from config import app
from routes import *

market = Market("BRL")
game = 730

if __name__ == '__main__':
    
    i1 = Item.query.get(1)
    i1.preco_atual = market.get_lowest_price(i1.nome, game) #Pega o preço atual do item

    i2 = Item.query.get(2)
    i2.preco_atual = market.get_lowest_price(i2.nome, game)
    
    i3 = Item.query.get(3)
    i3.preco_atual = market.get_lowest_price(i3.nome, game)

    i4 = Item.query.get(4)
    i4.preco_atual = market.get_lowest_price(i4.nome, game)

    db.session.commit()

    app.run(debug=True)
