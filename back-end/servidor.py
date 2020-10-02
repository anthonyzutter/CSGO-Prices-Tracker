from steam_community_market import Market
from config import app
from routes import *

market = Market("BRL")
game = 730

if __name__ == '__main__':
    itens = Item.query.order_by(Item.id).all()
    for x in itens:
        x.preco_atual = market.get_lowest_price(x.nome, game) #Atualiza o preço atual do item

    db.session.commit()
    app.run(debug=True)
