# Criando dadtas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://docs.python.org/pt-br/3.10/library/datetime.html
# datetime.fromtimestamp(Unix Timestamp)
# 
# instalando o pytz
# pip install pytz types-pytz

from datetime import datetime

data_str_data = '2022/04/20 07:49:23'
data_str_fmt = '%Y/%m/%d %H:%M:%S'

# data = datetime(2022, 4, 12, 7, 49, 23)
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)