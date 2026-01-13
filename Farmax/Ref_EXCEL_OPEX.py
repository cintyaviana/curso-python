# ===============================================================================================================================
# ATUALIZAÇÃO DO RELATÓRIO ABERTURA DE GASTOS
# ===============================================================================================================================
# Este código é um script de automação de interface (RPA) escrito em Python.

"""
RPA: Automação Robótica de Processos, é uma tecnologia de software que usa "robôs" (bots) virtuais para imitar ações humanas e automatizar tarefas repetitivas e baseadas em regras.
"""

# ---------------------------------------------------------------------------------------------------------------------------------
# 1.0 Importação de Bibliotecas
# ---------------------------------------------------------------------------------------------------------------------------------

import time
# Usada para criar pausas e formatar horários nos logs.

import os
# Utilizada para manipular caminhos de arquivos e nomes de diretórios.

import win32com.client as win32
# A biblioteca principal de automação. Ela permite que o Python controle as ferramentas nativas do Windows/Excel.

# ---------------------------------------------------------------------------------------------------------------------------------
# 2.0 Configuração do Caminho
# ---------------------------------------------------------------------------------------------------------------------------------

CAMINHO_EXCEL = r"\\192.168.0.7\Farmax\Diretoria Administrativa - Financeira\Gerência FP&A\04 - Fechamento CAD\03 - Despesas\02 - Bases de Dados - Anual\01 - Abertura de Gastos (SLAR+Ajustes+Razão) Total Farmax + Negra Rosa\2025 - A.G (SLAR+Ajustes+Razão).xlsx"

# O prefixo r antes das aspas indica uma "raw string", usada para que o Python não confunda as barras invertidas (\).

TIMEOUT_REFRESH = 600  # 10 minutos de tempo máximo de espera

"""
É uma variável de configuração que define um limite máximo de segurança para a execução da tarefa.

Em automações (RPA), existe o risco de um processo entrar em um "loop" infinito ou travar por problemas externos (ex: o banco de dados não responde ou a rede caiu no meio da atualização).
"""

# ---------------------------------------------------------------------------------------------------------------------------------
# 3.0 O Fluxo de Execução
# ---------------------------------------------------------------------------------------------------------------------------------


def executar_refresh_excel():

    # Verifica se o arquivo existe
    # Se não existir (rede fora, arquivo movido, nome alterado, etc), o script para com uma mensagem clara.
    if not os.path.exists(CAMINHO_EXCEL):
        print("Arquivo Excel não encontrado. Verifique o caminho e a conexão de rede.")
        return

    # .exists: é uma função da biblioteca - os - usada para verificar a existência de um arquivo ou pasta no computador ou na rede antes de realizar qualquer ação.

    print(f"[{time.strftime('%H:%M:%S')}] Iniciando o refresh do arquivo Excel: {os.path.basename(CAMINHO_EXCEL)}")

    # .basename: serve para extrair apenas o nome do arquivo de um caminho completo. O os.path.basename vai ignorar todo o endereço da rede e as pastas, devolvendo apenas: 2025 - A.G (SLAR+Ajustes+Razão).xlsx

    # Inicializamos a variável para garantir que o 'finally' consiga acessá-la depois
    excel = None

    """
    Essa linha serve para que o comando excel.Quit() lá embaixo saiba se ele realmente precisa fechar o Excel ou se o Excel nem chegou a ser aberto. É o que chamamos de inicialização de variável.
    """

    # O try (em português, "tentar") funciona como um escudo protetor para o seu código. Ele é usado para cercar partes do script que podem falhar por motivos que fogem do seu controle.
    try:
        # 3.1 Iniciar o Excel
        excel = win32.Dispatch('Excel.Application')
        excel.DisplayAlerts = False
        excel.Visible = False

        """
        Dispatch: Serve para conectar o Python ao motor do Excel instalado no Windows.
        Isso permite usar funções nativas como o .RefreshAll() (que atualiza Power Queries e conexões).
        """

        # 3.2 Abrir a pasta de trabalho
        workbook = excel.Workbooks.Open(CAMINHO_EXCEL)

        # .Open: Ele solicita ao processo do Excel (que você iniciou com o Dispatch) que localize o ficheiro no caminho especificado e o abra. A partir desse momento, o Python passa a ter um "objeto" (que você chamou de workbook) para controlar aquela folha de cálculo específica

        # 3.3 Executar o Refresh de TODOS os dados
        print(
            f"[{time.strftime('%H:%M:%S')}] Atualizando conexões e Power Queries...")
        workbook.RefreshAll()

        inicio = time.time()
        excel.CalculateUntilAsyncQueriesDone()

        # CalculateUntilAsyncQueriesDone: este comando faz o Python esperar dinamicamente até que o Excel confirme que terminou todas as atualizações de fundo.

        # 3.4.1 Timeout de segurança
        if time.time() - inicio > TIMEOUT_REFRESH:
            raise Exception("Tempo máximo de atualização excedido (timeout).")

        # raise : O raise  é o comando que você usa para "fabricar" um erro de propósito. O Destino: Assim que o raise é disparado, o Python para o que está fazendo no try e pula direto para o except

        # 3.4.2 Fechar a pasta de trabalho e confirma o salvamento
        print(f"[{time.strftime('%H:%M:%S')}] Confirmando o salvamento e fechamento.")
        workbook.Close(SaveChanges=True)
        print(f"[{time.strftime('%H:%M:%S')}] Processo concluído com sucesso!")

    except Exception as e:
        # Captura erros (como caminho errado ou arquivo travado) sem interromper o sistema bruscamente
        print(
            f"[{time.strftime('%H:%M:%S')}] Ocorreu um erro durante a automação: {e}")

        """
        except Exception: Captura qualquer problema que aconteça dentro do bloco try (como o arquivo estar sendo usado por outra pessoa, a rede cair ou o Excel travar).

        as e: Pega a mensagem de erro técnica do Windows e guarda dentro da letra e.

        O print com f-string:

        time.strftime('%H:%M:%S'): Registra o horário exato do erro.

        {e}: Mostra na tela exatamente qual foi o erro (ex: "Arquivo não encontrado" ou "Acesso negado").
        """

    finally:
        # 3.5 Encerrar o Excel
        if excel is not None:
            excel.Quit()

            """
            Quit: Encerra o processo do Microsoft Excel. Se não usado no bloco finally, o Excel continuará rodando "fantasmagórico" na memória RAM do computador.
            """
            print(
                f"[{time.strftime('%H:%M:%S')}] Instância do Excel encerrada na memória.")


if __name__ == "__main__":
    executar_refresh_excel()
