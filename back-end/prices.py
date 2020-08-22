from steam_community_market import Market
#from flask_sqlalchemy import SQLAlchemy 
from models import Item
market = Market("BRL")
game = 730

i1 = Item.query.filter_by(id=1).first()
i2 = Item.query.filter_by(id=2).first()
i3 = Item.query.filter_by(id=3).first()
i4 = Item.query.filter_by(id=4).first()

print(f"Nome: {i1.nome}")
print(f"Preço: R$ {market.get_lowest_price(i1.nome, game)}")
print(f"Volume vendido nas ultimas 24 horas: {market.get_volume(i1.nome, game)} unidades\n")

print(f"Nome: {i2.nome}")
print(f"Preço: R$ {market.get_lowest_price(i2.nome, game)}")
print(f"Volume vendido nas ultimas 24 horas: {market.get_volume(i2.nome, game)} unidades\n")

print(f"Nome: {i3.nome}")
print(f"Preço: R$ {market.get_lowest_price(i3.nome, game)}")
print(f"Volume vendido nas ultimas 24 horas: {market.get_volume(i3.nome, game)} unidades\n")

print(f"Nome: {i4.nome}")
print(f"Preço: R$ {market.get_lowest_price(i4.nome, game)}")
print(f"Volume vendido nas ultimas 24 horas: {market.get_volume(i4.nome, game)} unidades\n")