from src.models.produto import Produto

class EstoqueService:
    def __init__(self, repo):
        self.repo = repo

    def cadastrar_produto(self, nome):
        if nome == "": 
            return "❌ [Service]: Erro! O nome não pode ser vazio."
        
        novo_p = Produto(nome) # Cria o objeto
        self.repo.salvar(novo_p) # Manda para o repository
        return "✅ [Service]: Produto validado e enviado ao banco!"