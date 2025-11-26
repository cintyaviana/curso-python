
import time
import os
import pyautogui

CAMINHO_PBIX = r"\\192.168.0.7\Farmax\Projetos Power BI\PMO\Projetos\OPEX.pbix"


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


if __name__ == "__main__":
    executar_refresh_powerbi()
