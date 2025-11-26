
import time
import os
import pyautogui
import win32com.client as win32

CAMINHO_PBIX = r"\\192.168.0.7\Farmax\Projetos Power BI\PMO\Projetos\OPEX.pbix"
CAMINHO_EXCEL = r"\\192.168.0.7\Farmax\Diretoria Administrativa - Financeira\Gerência FP&A\04 - Fechamento CAD\03 - Despesas\02 - Bases de Dados - Anual\01 - Abertura de Gastos (SLAR+Ajustes+Razão) Total Farmax + Negra Rosa\2025 - A.G (SLAR+Ajustes+Razão).xlsx"


def executar_refresh_powerbi():

    print(f"[{time.strftime('%H:%M:%S')}] Abrindo o arquivo OPEX.pbix...")

    # 1. Abrir o arquivo PBIX usando os.startfile para abrir o arquivo no Windows
    os.startfile(CAMINHO_PBIX)

    time.sleep(90)

    # 2. Aguardar o refresh terminar
    print(f"[{time.strftime('%H:%M:%S')}] Aguardando a conclusão do refresh.")
    print("Mantenha o Power BI visível e o mouse/teclado inativos durante este período.")
    time.sleep(720)

    # 3. Fechar o Power BI Desktop
    print(f"[{time.strftime('%H:%M:%S')}] Fechando o Power BI Desktop.")
    pyautogui.hotkey('alt', 'f4')

    print(f"[{time.strftime('%H:%M:%S')}] Confirmando o salvamento e fechamento.")
    pyautogui.press('enter')
    time.sleep(90)

    print(f"[{time.strftime('%H:%M:%S')}] Processo concluído com sucesso!")


def executar_refresh_excel():
    print(f"[{time.strftime('%H:%M:%S')}] Iniciando o refresh do arquivo Excel: {os.path.basename(CAMINHO_EXCEL)}")

    # 1. Iniciar o Excel
    excel = win32.Dispatch('Excel.Application')
    excel.Visible = False  # Mantém o Excel invisível (True para ver)
    excel.DisplayAlerts = False  # Suprime alertas

    # 2. Abrir a pasta de trabalho (Workbook)
    print(f"[{time.strftime('%H:%M:%S')}] Abrindo a pasta de trabalho...")
    workbook = excel.Workbooks.Open(CAMINHO_EXCEL)

    # 3. Executar o Refresh de TODOS os dados
    print(f"[{time.strftime('%H:%M:%S')}] Executando o refresh de todas as conexões/modelos de dados.")
    workbook.RefreshAll()

    # 4. Aguardar a conclusão do refresh (melhor prática que time.sleep fixo)
    refresh_time_start = time.time()
    while excel.CalculationState != win32.constants.xlDone:
        print(f"[{time.strftime('%H:%M:%S')}] Aguardando... (Passaram {int(time.time() - refresh_time_start)} segundos)")
        time.sleep(5)

    print(f"[{time.strftime('%H:%M:%S')}] Refresh concluído.")

    # 5. Salvar o arquivo
    print(f"[{time.strftime('%H:%M:%S')}] Salvando o arquivo atualizado...")
    workbook.Save()

    # 6. Fechar a pasta de trabalho e encerrar o Excel
    print(f"[{time.strftime('%H:%M:%S')}] Fechando a pasta de trabalho e encerrando o Excel.")
    workbook.Close(SaveChanges=False)  # Já salvamos explicitamente
    excel.Quit()

    print(f"[{time.strftime('%H:%M:%S')}] Processo do Excel concluído com sucesso!")


if __name__ == "__main__":
    executar_refresh_powerbi()
    executar_refresh_excel()
