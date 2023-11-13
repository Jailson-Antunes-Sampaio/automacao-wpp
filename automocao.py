
import pyautogui
import time
import pandas as pd
from datetime import datetime
from win10toast_click import ToastNotifier

# Variaveis
link = "https://web.whatsapp.com/"
excel = pd.read_excel("Automocao_py.xlsm")
dt = datetime.now()
rept_time = 5
notification = False
linhas_excel = []
confidence = 0.9


def open_notification():
    global linhas_excel
    for lin in linhas_excel:
        pyautogui.PAUSE = 1.1
        # localizar imagen
        img_icone_chrome = pyautogui.locateCenterOnScreen(
            "iconechrome.png", confidence=confidence)

        if img_icone_chrome == None:
            img_chrome = pyautogui.locateCenterOnScreen(
                "chrome.png", confidence=confidence)
            pyautogui.click(img_chrome.x, img_chrome.y)

            img_icone_chrome = pyautogui.locateCenterOnScreen(
                "iconechrome.png", confidence=confidence)
            if img_icone_chrome == None:
                pyautogui.move(-120, -120)
                pyautogui.click()
        img_whats = pyautogui.locateCenterOnScreen(
            "whatsapp.png", confidence=confidence)
        pyautogui.click(img_whats.x, img_whats.y)
        img_pesq_whats = pyautogui.locateCenterOnScreen(
            "Captura.png", confidence=confidence)
        pyautogui.click(img_pesq_whats.x, img_pesq_whats.y)
        msg = excel.loc[lin, "Grupo"]
        pyautogui.write(msg)
        time.sleep(1)
        pyautogui.press("enter")

        pyautogui.write(excel.loc[lin, "Msg"])
        pyautogui.press("enter")

# Executando função para verificar se existe msg a ser enviada

def exec_whats():
    global linhas_excel
    global notification
    print("Inicio funcao")
    for linha in excel.index:
        if linha == 0:
            rept_time = excel.loc[linha, "rept_time"]

        day_week = excel.loc[linha, "Num_Dia_Semana"]
        hora_min = excel.loc[linha, "Hora"]

        if type(hora_min) == float:
            return
        dt = datetime.now()

        min = hora_min.minute
        hora = hora_min.hour
        dt_hora = dt.hour
        dt_min = dt.minute
        dt_min_sub = dt_min - rept_time

        print("Alimentou as variaveis")
        if day_week == dt.weekday():
            print("Entrou no primeiro IF")
            if hora == dt_hora:
                print("Entrou no Segundo IF")
                if min >= dt_min_sub and min <= dt_min:
                    linhas_excel.append(linha)
                    if not notification:
                        toaster = ToastNotifier()
                        notification = True
                        toaster.show_toast(
                            "Execução robo",  # title
                            excel.loc[linha, "Msg"],  # message
                            icon_path=None,  # 'icon_path'
                            duration=5,  # for how many seconds toast should be visible; None = leave notification in Notification Center
                            threaded=True,  # True = run other code in parallel; False = code execution will wait till notification disappears
                            callback_on_click=open_notification  # click notification to run function
                        )

                        print("Entrou no Terceiro IF")


exec_whats()

# pyautogui. hotkey('win','d')