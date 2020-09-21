from config import *

class Aviao(db.Model):
 
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    modelo = db.Column(db.String(20))
    lancamento = db.Column(db.String(20))
    velocidade_maxima = db.Column(db.String(100))
    capacidade_passageiro = db.Column(db.String(20))
    

    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " + self.modelo + ", " + self.lancamento + ", " +\
             self.velocidade_maxima + ", " + self.capacidade_passageiro 
    
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "modelo": self.modelo,
            "lancamento": self.lancamento,
            "velocidade_maxima": self.velocidade_maxima,
            "capacidade_passageiro": self.capacidade_passageiro,
            
        }

if __name__ == "__main__":
    
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    a1= Aviao(nome = "BAC/ Aerospatiale Concorde", modelo = "883", lancamento = "2003", velocidade_maxima = "2.179 km/h", capacidade_passageiro = "120")
    a2= Aviao(nome = "BvC/ Aerospatiale Concorde", modelo = "883", lancamento = "2003", velocidade_maxima = "2.179 km/h", capacidade_passageiro = "120")

    db.session.add(a1)
    db.session.add(a2)
    db.session.commit()

    print(a1)

    print(a1.json())
