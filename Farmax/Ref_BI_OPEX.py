
# ===============================================================================================================================
# ATUALIZAÇÃO DO RELATÓRIO BI OPEX
# ===============================================================================================================================
# Este código é um script de automação de interface (RPA) escrito em Python.

"""
RPA: Automação Robótica de Processos, é uma tecnologia de software que usa "robôs" (bots) virtuais para imitar ações humanas e automatizar tarefas repetitivas e baseadas em regras.
"""


# ---------------------------------------------------------------------------------------------------------------------------------
# 1.0 Importação de Bibliotecas
# ---------------------------------------------------------------------------------------------------------------------------------

import time
# Usada para criar pausas (sleep), necessárias para que o computador tenha tempo de processar as tarefas antes do próximo comando.

import os
# Utilizada para manipular caminhos de arquivos e abrir o sistema operacional.

import pyautogui
# A biblioteca principal de automação de interface. Ela "toma o controle" do mouse e teclado.

# ---------------------------------------------------------------------------------------------------------------------------------
# 2.0 Configuração do Caminho
# ---------------------------------------------------------------------------------------------------------------------------------

CAMINHO_PBIX = r"\\192.168.0.7\Farmax\Projetos Power BI\PMO\Projetos\OPEX.pbix"

# O prefixo r antes das aspas indica uma "raw string", usada para que o Python não confunda as barras invertidas (\) com comandos de código.

# ---------------------------------------------------------------------------------------------------------------------------------
# 3.0 O Fluxo de Execução
# ---------------------------------------------------------------------------------------------------------------------------------


def executar_refresh_powerbi():
    print(f"[{time.strftime('%H:%M:%S')}] Iniciando o refresh do arquivo pbix: {os.path.basename(CAMINHO_PBIX)}")

    # 3.1 Abrir o arquivo PBIX
    os.startfile(CAMINHO_PBIX)

    # 3.2 Aguardar o refresh terminar
    print(f"[{time.strftime('%H:%M:%S')}] Aguardando a conclusão do refresh.")
    time.sleep(840)

    # 3.3 Fechar o Power BI Desktop
    print(f"[{time.strftime('%H:%M:%S')}] Confirmando o salvamento e fechamento.")
    pyautogui.hotkey('alt', 'f4')
    time.sleep(15)

    # O comando hotkey (tecla de atalho) serve para combinações de teclas que precisam ser pressionadas ao mesmo tempo.

    pyautogui.press('enter')
    time.sleep(15)

    # O comando press (pressionar) serve para uma única tecla.

    print(f"[{time.strftime('%H:%M:%S')}] Processo do Power BI concluído com sucesso!")


if __name__ == "__main__":
    executar_refresh_powerbi()
