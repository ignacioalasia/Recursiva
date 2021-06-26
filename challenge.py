#1. Cantidad total de personas registradas.
#2. El promedio de edad de los socios de Racing.
#3. Un listado con las 100 primeras personas casadas, con estudios Universitarios,
# ordenadas de menor a mayor según su edad. Por cada persona, mostrar: nombre, edad y equipo.
#4. Un listado con los 5 nombres más comunes entre los hinchas de River.
#5. Un listado, ordenado de mayor a menor según la cantidad de socios, que enumere, 
# junto con cada equipo, el promedio de edad de sus socios, la menor edad registrada y la mayor edad registrada.

import pandas as pd
from operator import itemgetter


headers = ['nombre', 'edad', 'equipo', 'estado civil', 'nivel de estudios']
df = pd.read_csv('socios.csv', delimiter=';', encoding='latin1', names=headers)

edades = [] 
casados = []
nombres_comunes = []
equipos = df['equipo'].unique()
dict_equipos = {}
for equipo in equipos:
	dict_aux = {}
	dict_aux = {equipo : {'total' : 0,
						  'mayor_edad' : -1,
						  'menor_edad' : 9999,
						  'promedio_edad' : 0,
						  'suma_edades' : 0
						  }
				}
	dict_equipos.update(dict_aux)
for index, row in df.iterrows():
	if row['equipo'].lower() == 'racing':
		 if row['edad']:
		 	edades.append(int(row['edad']))
	if index<100:
		if(row['estado civil'].lower() == 'casado') and (row['nivel de estudios'].lower() == 'universitario'):
			casado = {}
			casado = {'Nombre' : row['nombre'],
					  'Edad' : row['edad'],
					  'Equipo' : row['equipo']}
			casados.append(casado)
	if row['equipo'].lower() == 'river':
		 if row['nombre']:
		 	nombres_comunes.append(row['nombre'])
	for equipo in equipos:
		if row['equipo'] == equipo:
			dict_equipos[equipo]['total'] += 1
			
			if dict_equipos[equipo].get('mayor_edad'):
				if int(row['edad']) > int(dict_equipos[equipo].get('mayor_edad')):
					dict_equipos[equipo]['mayor_edad'] = row['edad']
			if dict_equipos[equipo].get('menor_edad'):
				if int(row['edad']) < int(dict_equipos[equipo].get('menor_edad')):
					dict_equipos[equipo]['menor_edad'] = row['edad']
			dict_equipos[equipo]['suma_edades'] += row['edad']

for estadistica in dict_equipos:
	promedio = dict_equipos[estadistica]['suma_edades'] // dict_equipos[estadistica]['total']
	dict_equipos[estadistica].pop('suma_edades')
	dict_equipos[estadistica]['promedio_edad'] = promedio
	
			

nombre_mas_repetido = []
for i in range(0,5):
	nombre_mas_repetido.append(max(set(nombres_comunes), key = nombres_comunes.count))
	nombres_comunes = [s for s in nombres_comunes if s != nombre_mas_repetido[i]]


print (f'1. Hay {len(df)} personas en el .csv')
#print (edades)
#print(f'{sum(edades)}')
#promedio = sum(edades)/len(edades)
print(f'2. El promedio de las edades de los hinchas de racing es {sum(edades)/len(edades)}')
print(f"3. Listado de las 100 personas casadas: {sorted(casados, key = lambda i: i['Edad'])}")
print(f'4. Los 5 nombres mas repetidos de river son: {nombre_mas_repetido}')  
print(f'5. Listado: {dict_equipos}')
