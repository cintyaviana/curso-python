import time
import os
import pyautogui
import win32com.client as win32

CAMINHO_PBIX = r"\\192.168.0.7\Farmax\Projetos Power BI\PMO\Projetos\OPEX.pbix"
CAMINHO_EXCEL = r"\\192.168.0.7\Farmax\Diretoria Administrativa - Financeira\Gerência FP&A\04 - Fechamento CAD\03 - Despesas\02 - Bases de Dados - Anual\01 - Abertura de Gastos (SLAR+Ajustes+Razão) Total Farmax + Negra Rosa\2025 - A.G (SLAR+Ajustes+Razão).xlsx"


def executar_refresh_powerbi():
    print(f"[{time.strftime('%H:%M:%S')}] Iniciando o refresh do arquivo pbix: {os.path.basename(CAMINHO_PBIX)}")

    # 1. Abrir o arquivo PBIX
    os.startfile(CAMINHO_PBIX)

    # 2. Aguardar o refresh terminar
    print(f"[{time.strftime('%H:%M:%S')}] Aguardando a conclusão do refresh (Estimativa: 6 min).")
    time.sleep(300)

    # 3. Fechar o Power BI Desktop
    print(f"[{time.strftime('%H:%M:%S')}] Confirmando o salvamento e fechamento.")
    pyautogui.hotkey('alt', 'f4')
    time.sleep(15)

    pyautogui.press('enter')
    time.sleep(15)

    print(f"[{time.strftime('%H:%M:%S')}] Processo do Power BI concluído com sucesso!")


def executar_refresh_excel():
    print(f"[{time.strftime('%H:%M:%S')}] Iniciando o refresh do arquivo Excel: {os.path.basename(CAMINHO_EXCEL)}")

    # 1. Iniciar o Excel
    excel = win32.Dispatch('Excel.Application')
    excel.Visible = True  # Mantém o Excel visível (True para ver)
    excel.DisplayAlerts = False  # Suprime alertas

    # 2. Abrir a pasta de trabalho
    workbook = excel.Workbooks.Open(CAMINHO_EXCEL)

    # 3. Executar o Refresh de TODOS os dados
    print(f"[{time.strftime('%H:%M:%S')}] Aguardando a conclusão do refresh (Estimativa: 5 min).")
    workbook.RefreshAll()
    time.sleep(300)

    # 4. Fechar a pasta de trabalho e encerrar o Excel
    print(f"[{time.strftime('%H:%M:%S')}] Confirmando o salvamento e fechamento.")
    workbook.Close(SaveChanges=True)
    excel.Quit()

    print(f"[{time.strftime('%H:%M:%S')}] Processo do Excel concluído com sucesso!")


if __name__ == "__main__":
    executar_refresh_powerbi()
    executar_refresh_excel()
