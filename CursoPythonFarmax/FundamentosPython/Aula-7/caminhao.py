
# ===========MECANISMO DE HERANÇA ENTRE CLASSES ================================================

# 1 - PARA QUE EXISTA A HERANÇA ENTRE CLASSES É NECESSÁRIO QUE EXISTA UMA "RELAÇÃO" DIRETA ENTRE ESTAS CLASSES

# para que seja possível estabelecer uma "relação" entre as classes Caminhao() e Automovel() será preciso, aqui, "trazer" a classe Automovel para fazer parte desta estrutura de código. Isso se dá fazendo a "importação" da classe Automovle - a partir de seu arquivo de origem.
# aqui, neste ponto, acabamos de estabelecer a relação entre as classes Caminhao() e Automovel()
from automovel import Automovel

"""
# 2 -

a) a classe Caminhao() pode "herdar" tudo aquilo que pertence a classe Automovel, ou seja, a classe Caminhao pode acessar e fazer uso de
qualqeur recurso descrito dentro da classe Automovel()

b) para que essa dinâmica de funcionamento ocorra será necessário estabelecer esta herança

"""

# definir a classe Caminhao() - até este momento (momento da definição da classe Caminhao) esta classe é uma classe comum


class Caminhao(Automovel):  # aqui, neste momento em que a classe Automovel é descrita entre os parenteses da classe Caminhao, ocorre a herança entre as classes

    # esta é uma instrução de nulidade - significa, literalmente, "não faça nada aqui"; esta instrução é usada sempre que, numa estrutura de classe/função/loop/if/etc., não queremos colocar nenhum outra instrução, por hora.
    pass


"""
Acima, no mecanismo de herança estabelecido entre Caminhao() e Automovel, passa a existir uma relação hierarquica-familiar:
a) a classe Caminhao se torna "filha" da classe Automovel
b) por sua vez, a classe Automovel, se torna "pai/mãe" da classe Caminhao()
c) esta relação hierarquica-familiar também pode receber outras nomenclaturas, por exemplo: superclasse (Automovel)/subclasse (Caminhao); classe-base(Automovel)/classe-derivada(Caminhao)
"""

# =========== TESTANTO O MECANISMO DE HERANÇA ===============

# definir o objeto da classe Caminhao()
caminhao1 = Caminhao('Scania', 'Modelo Scania', 2022)

# exibir estes valores
print(caminhao1.exibicao())
