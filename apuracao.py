import pandas as pd
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Executado em =", current_time)

df = pd.read_json('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

print("Urnas apuradas: {urnas}%".format(urnas = df['pesi'][0]))


for i in range(11):
	string = ("Nome: {name} ".format(name = df['cand'][i]['nm']))
	string += ("Votos: {votes} ".format(votes = df['cand'][i]['vap']))
	string += ("Percentual: {percent}\n".format(percent = df['cand'][i]['pvap']))
	print(string)
	string = ''
