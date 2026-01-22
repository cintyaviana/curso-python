
# ===============================================================================================================================
# CENTRO DE COMANDO DE RPA
# ===============================================================================================================================

# ===============================================================================================================================
# 1.0 IMPORTAÇÃO DAS BIBLIOTECAS
# ===============================================================================================================================

import time
# Usada para criar pausas (sleep), necessárias para que o computador tenha tempo de processar as tarefas antes do próximo comando.

import os
# Utilizada para manipular caminhos de arquivos e abrir o sistema operacional.

import pyautogui
# A biblioteca principal de automação de interface. Ela "toma o controle" do mouse e teclado.

import webbrowser
# A biblioteca abre uma URL no navegador.

import threading

import psutil

import win32com.client as win32

import win32process

# ======================================================================
# 2.0 CAMINHOS DAS BASES DE DADOS
# ======================================================================

CAMINHO_EXCEL_NAO_RECORRENTE = r"\\192.168.0.7\Farmax\Diretoria Administrativa - Financeira\Gerência FP&A\04 - Fechamento CAD\03 - Despesas\02 - Bases de Dados - Anual\03- Não Recorrente\2025- Não recorrente.xlsx"

CAMINHO_EXCEL_AJUSTE_GERENCIAL = r"\\192.168.0.7\Farmax\Diretoria Administrativa - Financeira\Gerência FP&A\04 - Fechamento CAD\03 - Despesas\02 - Bases de Dados - Anual\02 - Ajustes Manuais Consolidado Farmax + Negra Rosa\2025 - Ajustes Manuais Consolidado.xlsx"

CAMINHO_EXCEL_DESPESAS = r"\\192.168.0.7\Farmax\Diretoria Administrativa - Financeira\Gerência FP&A\04 - Fechamento CAD\03 - Despesas\02 - Bases de Dados - Anual\01 - Abertura de Gastos (SLAR+Ajustes+Razão) Total Farmax + Negra Rosa\2026 - A.G (SLAR+Ajustes+Razão).xlsx"

CAMINHO_PBIX = r"\\192.168.0.7\Farmax\Projetos Power BI\PMO\Projetos\OPEX.pbix"

# ======================================================================
# 3.0 ATUALIZAÇÃO BASES EXCEL
# ======================================================================

# ----------------------------------------------------------------------
# 3.1 INICIALIZAÇÃO
# ----------------------------------------------------------------------


def get_excel_pid(excel):
    hwnd = excel.Hwnd
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    return pid


def watchdog_excel(pid, timeout, flag):
    inicio = time.time()
    while not flag["done"]:
        if time.time() - inicio > timeout:
            try:
                psutil.Process(pid).kill()
            except:
                pass
            flag["killed"] = True
            return
        time.sleep(5)


def criar_excel():
    excel = win32.DispatchEx("Excel.Application")
    excel.DisplayAlerts = False
    excel.Visible = True
    return excel

# ----------------------------------------------------------------------
# 3.2 Refresh
# ----------------------------------------------------------------------


def refresh_excel(caminho, timeout):
    excel = criar_excel()
    try:
        if not os.path.exists(caminho):
            print(f"Arquivo não encontrado: {caminho}")
            return

        nome = os.path.basename(caminho)
        print(f"[{time.strftime('%H:%M:%S')}] Abrindo {nome}")

        wb = excel.Workbooks.Open(caminho)
        print(f"[{time.strftime('%H:%M:%S')}] Atualizando dados...")

        flag = {"done": False, "killed": False}
        pid = get_excel_pid(excel)
        threading.Thread(target=watchdog_excel, args=(
            pid, timeout, flag), daemon=True).start()

        try:
            wb.RefreshAll()
            excel.CalculateUntilAsyncQueriesDone()

            if flag["killed"]:
                raise Exception("Excel travou durante o refresh.")

            wb.Save()
            wb.Close(SaveChanges=True)
            print(f"[{time.strftime('%H:%M:%S')}] {nome} atualizado com sucesso.")

        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] FALHA no refresh de {nome}: {e}")

        finally:
            flag["done"] = True

    finally:
        try:
            excel.Quit()
        except:
            pass

    # O prefixo r antes das aspas indica uma "raw string", usada para que o Python não confunda as barras invertidas (\) com comandos de código.

# ======================================================================
# 4.1 ATUALIZAÇÃO BASES POWER BI OPEX
# ======================================================================


def refresh_powerbi():
    print(f"[{time.strftime('%H:%M:%S')}] Iniciando o refresh do arquivo pbix: {os.path.basename(CAMINHO_PBIX)}")

    # 3.1 Abrir o arquivo PBIX
    os.startfile(CAMINHO_PBIX)

    # 3.2 Aguardar o refresh terminar
    print(f"[{time.strftime('%H:%M:%S')}] Aguardando a conclusão do refresh.")
    time.sleep(900)

    # 3.3 Fechar o Power BI Desktop
    print(f"[{time.strftime('%H:%M:%S')}] Confirmando o salvamento e fechamento.")
    pyautogui.hotkey('alt', 'f4')
    time.sleep(15)

    # O comando hotkey (tecla de atalho) serve para combinações de teclas que precisam ser pressionadas ao mesmo tempo.

    pyautogui.press('enter')
    time.sleep(15)

    # O comando press (pressionar) serve para uma única tecla.

    print(f"[{time.strftime('%H:%M:%S')}] Processo do Power BI concluído com sucesso!")

# ======================================================================
# 5.1 ABERTURA DE PÁGINAS WEB
# ======================================================================

# ----------------------------------------------------------------------
# 5.1 Página Web BI Administrador
# ----------------------------------------------------------------------


def abrir_pagina_BI_Adm():
    url = "https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?client_id=b01ec068-b8bc-4e15-ab9b-7e7c9b447e8c&redirect_uri=https%3A%2F%2Fadmin.powerembedded.com.br%2Fsignin-oidc&response_type=code&scope=openid%20profile%20offline_access%20user.read&code_challenge=IOnfVKLzYhiO440lLNKDN8YdtEsWEipvJmL-es5Bac0&code_challenge_method=S256&response_mode=form_post&nonce=639045918900533874.YTE3ZDA3ZDEtMzE3OS00NWZmLWJmNzktNjA1YTlkYTRjMGE5YTM3ODBmNTYtNzk2ZC00NGRmLTg4ZjYtNWU0NzhiZGU2MzNi&client_info=1&x-client-brkrver=IDWeb.3.1.0.0&state=CfDJ8OB2wUn7P0lNmazrWZUs2M61t1gorWpIt_czjYZ1sg1yOj4mkspJm0B7AFI5PTDqXZSvvP9jF7IdHQTE75RTCeUoOA8fKK-hIkMROBVL0VS_ZgZoMR9gVVXcNmElK8CDJ26Dof6OhHB8YKpRpB3cUNZjtFGcoJfNrxbuln8Oaa9KzNbLcdcUULAV0SUE2HT0_Eptptl1Tsyd3quqTvjWqJKtrPVYE3QTWqHFiZKcM0zjBvr4p3UzG2cdi7zYjGdFZSXJiCpGRrOWPk0F9PAxsyzxWx9KUtOprnSN3wu4hNQWUzz9lRWQEKYMs9VAJjq-o0-rUUyodH5hIaOOx7PjeKVuUXnYTu7-EdTFLlI3bkLSEh3QbOqlJ5-3OWhDQneIqWx_C4S7dBkNSrKRD0X7FCE&x-client-SKU=ID_NET8_0&x-client-ver=8.0.2.0&sso_reload=true"

    webbrowser.open(url)

# ----------------------------------------------------------------------
# 5.2 Página Web BI OPEX
# ----------------------------------------------------------------------


def abrir_pagina_BI_OPEX():
    url = "https://bi.farmax.com.br/Organization/9d22151a-168a-4aa9-9447-1cdd032a1f8c/Favorites"

    webbrowser.open(url)

# ----------------------------------------------------------------------
# 5.3 Página Web Linkedin
# ----------------------------------------------------------------------


def abrir_pagina_Linkedin():
    url = "https://www.linkedin.com/feed/"

    webbrowser.open(url)


if __name__ == "__main__":
    refresh_powerbi()
    # refresh_excel(CAMINHO_EXCEL_NAO_RECORRENTE, 900)
    # refresh_excel(CAMINHO_EXCEL_AJUSTE_GERENCIAL, 900)
    refresh_excel(CAMINHO_EXCEL_DESPESAS, 1200)
    abrir_pagina_BI_Adm()
    abrir_pagina_BI_OPEX()
    abrir_pagina_Linkedin()
