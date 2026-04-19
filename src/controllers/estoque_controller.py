class EstoqueController:
    def __init__(self, service):
        self.service = service

    def clicar_no_botao_salvar(self, nome_digitado):
        # Apenas repassa a ordem
        return self.service.cadastrar_produto(nome_digitado)