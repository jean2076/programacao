from config import *
from modelo import Aviao

@app.route("/")
def inicio():
    return 'Sistema de cadastro de Avião. '+\
        '<a href="/listar_aviao">Cheque aqui os listados</a>'

@app.route("/listar_aviao")
def listar_aviao():
   
    avioes = db.session.query(Aviao).all()
 
    avioes_em_json = [ x.json() for x in avioes ]
 
    resposta = jsonify(avioes_em_json)
 
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

app.run(debug=True)