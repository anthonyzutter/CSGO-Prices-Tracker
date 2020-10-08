from config import *
from models import Item
from servidor import market, game

@app.route("/")
def inicio():
    return 'Sistema para cadastrar itens. '+\
        '<a href="/listar_itens">Listar Itens</a>'

@app.route("/listar_itens")
def listar_itens():
    itens = db.session.query(Item).all()
    retorno = []
    for i in itens:
        retorno.append(i.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/incluir_item", methods=['POST'])
def incluir_item():
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    dados = request.get_json()
    try:
        nova = Item(**dados)
        db.session.add(nova)
        db.session.commit()
        nova.url += nova.nome
        nova.preco_atual = market.get_lowest_price(nova.nome, game) 
        db.session.commit()
    except Exception as e: 
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/excluir_item/<int:item_id>", methods=['DELETE'])
def excluir_item(item_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Item.query.filter(Item.id == item_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta