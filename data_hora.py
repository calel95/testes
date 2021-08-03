from datetime import date, time, datetime, timedelta

#traz a data atual no modelo Amarican yyyy-mm-dd
def working_with_dates():
    data_atual = date.today()
    print(data_atual)
    #com o srtftime pode escolher o formato da data, opções estao na documentação datetime
    data_atual2 = date.today()
    print(data_atual2.strftime('%d/%m/%Y'))

def working_with_times():
    horario = time(hour=15, minute=18, second=30) #aqui a gente cria um horario que quiser
    print(horario)
#alem do strftime poder deixar o formato do date or time do jeito que quisermos, ele converte para str
    print(horario.strftime('%H - %M - %S'))

#datetime apresenta a data e o horario atual
def working_with_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('Data: %d-%m-%Y Horario: %H:%M:%S'))
    print(data_atual.day)
    data_criada = datetime(1995, 1,19, 2,16,44)
    print(data_criada)
    data_string = '01/01/2019' #é possivel colocar o horario tbm caso queira
    #faz a conversao da data no formato de string para formato data, strptime deixa como quisermos o formato
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)

#podemos adicionar dias, horas, meses, subtrair e somar datas e horarios
def calculate_date():
    data_string = '01/01/2019'  # é possivel colocar o horario tbm caso queira
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    #adicionando 365 dias a data_string
    nova_data = data_convertida + timedelta(days=365)
    print(nova_data)

#working_with_times()
#working_with_dates()
#working_with_datetime()
calculate_date()