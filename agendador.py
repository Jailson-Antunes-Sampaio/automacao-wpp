# from plyer import notification
# import time

# title = 'Notificação '
# message = 'Robo Jack'

# notification.notify(title=title, message=message)

# # Aguarda por 5 segundos antes de fechar a notificação (opcional)
# time.sleep(10)

import os
import pandas as pd 
from datetime import datetime

excel = pd.read_excel("Automocao_py.xlsm")

def agendador_tarefa(hora):
    # Defina a data e hora para agendar a tarefa (substitua com a data e hora desejadas)

    now = datetime.now()
    data = f"{str(now.day).zfill(2)}/{str(now.month).zfill(2)}/{now.year}"
    data_nome = f"{now.day}-{now.month}-{now.year}"
    hora_nome = f"{hora.hour}-{hora.minute}"
    # Nome da tarefa a ser excluída
    nome_tarefa =  f"automacao-{data_nome}-{hora_nome}"
    try :
        # Comando para excluir a tarefa agendada
        command = f'schtasks /delete /tn {nome_tarefa} /f'

        # Execute o comando usando o módulo os
        os.system(command)
    except:
        pass

    # Comando para criar a tarefa agendada para uma data e hora específicas
    command = f'schtasks /create /sc once /sd {data} /st {hora} /tn {nome_tarefa} /tr "C:\\Users\\antun\\OneDrive\\Documentos\\Projetos\\robo_jack\\script.bat"'

    # Execute o comando usando o módulo os
    os.system(command)


def exec_agendador():
    print("Inicio funcao")
    for linha in excel.index:

        day_week = excel.loc[linha, "Num_Dia_Semana"]
        hora_min = excel.loc[linha, "Hora"]

        if type(hora_min) == float:
            return
        dt = datetime.now()

        print("Alimentou as variaveis")
        if day_week == dt.weekday():
            print("Entrou no primeiro IF")
            
            agendador_tarefa(hora_min)            
exec_agendador()

