# ======================================================================
# JOGO JOKENPÔ
# ======================================================================
# Importamos a biblioteca para gerar escolhas aleatórias
import random

from typing import Tuple, Optional

# ----------------------------------------------------------------------
# Declaração de variáveis
# ----------------------------------------------------------------------
PEDRA = "PEDRA"
PAPEL = "PAPEL"
TESOURA = "TESOURA"

# Criação de uma tupla para o computador escolher
OPCOES = (PEDRA, PAPEL, TESOURA)

# Criação de um dicionário
REGRAS = {
    PEDRA: {"vence": TESOURA, "acao": "quebrando-a"},
    TESOURA: {"vence": PAPEL, "acao": "cortando-o"},
    PAPEL: {"vence": PEDRA, "acao": "cobrindo-a"},
}

RESULTADO_EMPATE = "EMPATE"
RESULTADO_JOGADOR = "JOGADOR"
RESULTADO_COMPUTADOR = "COMPUTADOR"

# ----------------------------------------------------------------------
# Função de formatação, para padronização de textos. Ele define uma função que recebe uma string (texto) e a devolve formatada.
# ----------------------------------------------------------------------


def formatar_jogada(jogada: str) -> str:
    return jogada.capitalize()


"""
jogada: str = Isso é um type hint. Ele indica que a função espera receber um argumento chamado jogada que seja do tipo string (texto).
-> str: = Indica que o que a função devolve (retorno) também será uma string
O método .capitalize() = 
    -Transforma a primeira letra em maiúscula.
    -Transforma todas as outras letras em minúsculas.
"""
# ----------------------------------------------------------------------
# Função de exibição do placar
# ----------------------------------------------------------------------


def exibir_placar(vitorias: int, derrotas: int, empates: int) -> None:
    print("\n" + "=" * 30)
    print(f"PLACAR: Você: {vitorias} x CPU: {derrotas} | Empates: {empates}")
    print("=" * 30)

    """
    -> None = O None no Python representa a ausência de um valor. Quando você o vê naquela posição do código, ele está indicando o que a função devolve após ser executada.

    Existem dois tipos principais de funções:
    Funções que processam e entregam algo: Como uma função de soma, que te devolve o resultado (2 + 2 = 4).
    Funções de "Ação": Como a sua exibir_placar. O objetivo dela é apenas imprimir algo na tela. Ela faz o trabalho dela e "morre" ali, sem enviar um valor de volta para o resto do programa.
    """

# ----------------------------------------------------------------------
# Regras de Negócio
# ----------------------------------------------------------------------


def processar_rodada(jogador: str) -> Tuple[str, str, Optional[str]]:
    """
    Processa uma rodada do jogo.

    Retorna:
        resultado (str): EMPATE | JOGADOR | COMPUTADOR
        computador (str): jogada do computador
        acao (str | None): ação da vitória, se houver
    """

    # Faz o computador escolher aleatoriamente entre Pedra, Papel ou Tesoura
    computador = random.choice(OPCOES)

    if jogador == computador:
        return RESULTADO_EMPATE, computador, None

    if REGRAS[jogador]["vence"] == computador:
        return RESULTADO_JOGADOR, computador, REGRAS[jogador]["acao"]

    return RESULTADO_COMPUTADOR, computador, REGRAS[computador]["acao"]

# ----------------------------------------------------------------------
# Camada de Aplicação
# ----------------------------------------------------------------------


def jogar() -> None:
    vitorias = 0
    derrotas = 0
    empates = 0

    print("🎮 BEM-VINDO AO JOKENPÔ!")

    while True:
        jogador = input(
            "\nEscolha Pedra, Papel, Tesoura (ou 'SAIR'): ").strip().upper()

        """
        O while True: é uma estrutura de controle usada para criar um loop (laço) infinito.

        Em programação, o while executa um bloco de código "enquanto" uma condição for verdadeira. Como o valor True é, por definição, sempre verdadeiro, o código dentro desse bloco nunca para de rodar por conta própria.
        """

        if jogador == "SAIR":
            print("\nObrigado por jogar! Placar final:")
            exibir_placar(vitorias, derrotas, empates)
            break

        if jogador not in OPCOES:
            print("❌ Opção inválida! Tente novamente.")
            continue

        resultado, computador, acao = processar_rodada(jogador)

        print(f"\n➔ Você: {formatar_jogada(jogador)}")
        print(f"➔ CPU:  {formatar_jogada(computador)}")

        if resultado == RESULTADO_EMPATE:
            print("🤝 Rodada empatada!")
            empates += 1

        elif resultado == RESULTADO_JOGADOR:
            print(
                f"✅ Você venceu! "
                f"{formatar_jogada(jogador)} vence "
                f"{formatar_jogada(computador).lower()} ({acao})."
            )
            vitorias += 1

        else:
            print(
                f"💻 O Computador venceu! "
                f"{formatar_jogada(computador)} vence "
                f"{formatar_jogada(jogador).lower()} ({acao})."
            )
            derrotas += 1

        exibir_placar(vitorias, derrotas, empates)


# ----------------------------------------------------------------------
# Ponto de Entrada
# ----------------------------------------------------------------------
if __name__ == "__main__":
    jogar()
