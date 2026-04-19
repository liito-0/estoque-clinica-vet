from src.repositories.produto_repository import ProdutoRepository
from src.services.estoque_service import EstoqueService
from src.controllers.estoque_controller import EstoqueController
from src.views.menu_view import MenuView

# 1. Criamos as instâncias (As peças)
banco = ProdutoRepository()
regra_de_negocio = EstoqueService(banco)
garcom = EstoqueController(regra_de_negocio)
tela = MenuView()

# 2. Fazemos o sistema rodar
valor_digitado = tela.exibir_tela()
resultado = garcom.clicar_no_botao_salvar(valor_digitado)
tela.mostrar_resultado(resultado)