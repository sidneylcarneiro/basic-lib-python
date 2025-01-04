from datetime import datetime, timedelta

hoje = datetime.now()
print("data completa:", hoje)
input()

data_hoje = hoje.date()
print("data AAAA-MM-DD:", data_hoje)
input()

dia_hoje = hoje.day
print("Dia de Hoje:", dia_hoje)
input()

mes_atual = hoje.month
print("Mês atual:", mes_atual)
input()

ano_atual = hoje.year
print("Ano atual:", ano_atual)
input()

hora_atual = str(hoje.hour)+":"+str(hoje.minute)+":"+str(hoje.second)
print("Horário atual:", hora_atual)
input()

print("Dia de Hoje + 1 (dia):", data_hoje + timedelta(days=1))
input()

data_do_contrato = datetime(day=1, month=9, year=2024)

atraso = hoje - data_do_contrato
print("Atraso em dias:", atraso.days)
input()

data_final = "01-08-2005"

data_final_datetime = datetime.strptime(data_final, "%d-%m-%Y")

print("Imprimir data final:", data_final_datetime)

print("Imprimir data formatada:", data_final_datetime.strftime("%d/%m/%Y"))

input()






























