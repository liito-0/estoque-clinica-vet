class ProdutoRepository:
    def __init__(self):
        self.lista_produtos = [] 

    def salvar(self, produto):
        self.lista_produtos.append(produto)
        print(f"📦 [Repository]: {produto.nome} foi guardado na lista.")