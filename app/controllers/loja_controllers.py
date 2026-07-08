
class LojaController:
    def get_vitrine(self, mercado):

        produtos_disponiveis = [
            p.to_dict() for p in mercado.lista_produtos if p.get_estoque() > 0
        ]
        return produtos_disponiveis


        
