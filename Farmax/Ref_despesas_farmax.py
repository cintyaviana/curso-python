# ---------------------------------------------------------------------------------------------------------------------------------
# 1.0 Importação de Bibliotecas
# ======================================================================

import time
import os
import threading
import psutil
import win32com.client as win32
import win32process

# ======================================================================
# CAMINHOS DAS BASES DE DADOS
# ======================================================================

CAMINHO_EXCEL_NAO_RECORRENTE = r"\\192.168.0.7\Farmax\Diretoria Administrativa - Financeira\Gerência FP&A\04 - Fechamento CAD\03 - Despesas\02 - Bases de Dados - Anual\03- Não Recorrente\2025- Não recorrente.xlsx"

CAMINHO_EXCEL_AJUSTE_GERENCIAL = r"\\192.168.0.7\Farmax\Diretoria Administrativa - Financeira\Gerência FP&A\04 - Fechamento CAD\03 - Despesas\02 - Bases de Dados - Anual\02 - Ajustes Manuais Consolidado Farmax + Negra Rosa\2025 - Ajustes Manuais Consolidado.xlsx"

CAMINHO_EXCEL_DESPESAS = r"\\192.168.0.7\Farmax\Diretoria Administrativa - Financeira\Gerência FP&A\04 - Fechamento CAD\03 - Despesas\02 - Bases de Dados - Anual\01 - Abertura de Gastos (SLAR+Ajustes+Razão) Total Farmax + Negra Rosa\2026 - A.G (SLAR+Ajustes+Razão).xlsx"

# ======================================================================
# UTILIDADES
# ======================================================================


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

# ======================================================================
# REFRESH
# ======================================================================


def refresh_excel_blindado(caminho, timeout):
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

# ======================================================================
# CHAMADA PARA EXECUÇÃO
# ======================================================================


if __name__ == "__main__":
    refresh_excel_blindado(CAMINHO_EXCEL_NAO_RECORRENTE, 900)
    refresh_excel_blindado(CAMINHO_EXCEL_AJUSTE_GERENCIAL, 900)
    refresh_excel_blindado(CAMINHO_EXCEL_DESPESAS, 1200)
