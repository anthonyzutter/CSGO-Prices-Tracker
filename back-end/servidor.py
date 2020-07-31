from config import *
from classe import Item

@app.route("/")
def inicio():
    return 'Sistema para cadastrar itens. '+\
        '<a href="/listar_itens">Listar Itens</a>'

@app.route("/listar_itens")
def listar_itens():
    itens = db.session.query(Item).all()
    itens_em_json = [ x.json() for x in itens ]
    resposta = jsonify(itens_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True)
