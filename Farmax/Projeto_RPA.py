# ======================================================================
# RPA – ATUALIZAÇÃO AUTOMÁTICA DE RELATÓRIO EXCEL
# ======================================================================
# Script de automação para atualização de conexões e Power Queries em Excel

# ----------------------------------------------------------------------
# 1. Importação de Bibliotecas
# ----------------------------------------------------------------------

import time
# Usada para criar pausas e registrar horários nos logs.

import os
# Utilizada para validar caminhos de arquivos.

import win32com.client as win32
# Biblioteca que permite que o Python controle o Excel via COM Automation.

# ----------------------------------------------------------------------
# 2. Configuração do Caminho
# ----------------------------------------------------------------------

CAMINHO_EXCEL = r"\\SERVIDOR\PASTA\Relatorio.xlsx"
# Caminho genérico apenas para fins de demonstração.

TIMEOUT_REFRESH = 600  # Tempo máximo de espera para atualização (em segundos)

# ----------------------------------------------------------------------
# 3. Fluxo de Execução
# ----------------------------------------------------------------------


def executar_refresh_excel():

    # Verifica se o arquivo existe antes de iniciar o processo
    if not os.path.exists(CAMINHO_EXCEL):
        print("Arquivo não encontrado.")
        return

    print(f"[{time.strftime('%H:%M:%S')}] Iniciando atualização do arquivo Excel.")

    # Inicializa as variáveis para garantir fechamento no finally
    excel = None
    workbook = None

    try:
        # Inicia a aplicação Excel
        excel = win32.Dispatch('Excel.Application')
        excel.DisplayAlerts = False
        excel.Visible = False

        # Abre o arquivo Excel
        workbook = excel.Workbooks.Open(CAMINHO_EXCEL)

        # Executa a atualização de todas as conexões e Power Queries
        print(f"[{time.strftime('%H:%M:%S')}] Atualizando conexões e consultas...")
        workbook.RefreshAll()

        inicio = time.time()
        excel.CalculateUntilAsyncQueriesDone()
        # Aguarda o Excel concluir todas as atualizações em segundo plano

        # Controle de tempo máximo de execução
        if time.time() - inicio > TIMEOUT_REFRESH:
            raise Exception("Tempo máximo de atualização excedido.")

        # Salva e fecha o arquivo
        print(f"[{time.strftime('%H:%M:%S')}] Salvando e fechando o arquivo.")
        workbook.Close(SaveChanges=True)

        print(f"[{time.strftime('%H:%M:%S')}] Processo finalizado com sucesso.")

    except Exception as e:
        # Captura e exibe qualquer erro ocorrido durante a automação
        print(f"[{time.strftime('%H:%M:%S')}] Erro durante a automação: {e}")

    finally:
        # Encerra a instância do Excel aberta pelo robô
        if excel:
            excel.Quit()
            print(f"[{time.strftime('%H:%M:%S')}] Excel encerrado.")


if __name__ == "__main__":
    executar_refresh_excel()
