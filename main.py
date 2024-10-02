import pandas as pd
import openpyxl
from tabulate import tabulate


dt=pd.read_excel("ejemplo.xlsx", sheet_name="Hoja1", header=None)
print(tabulate(dt))
#---Cuál es el nombre de los estudiantes de los primeros 12 registros---
#print(dt[0].head(13))

#---Cuál es el nombre de los estudiantes de los primeros 9 registros
#print(dt[0].head(10))

#---Muestre que estudiantes tienen falta
#print(tabulate(dt[(dt[2]==1) & (dt[3]==1) & (dt[4]==1)]))

#---Muestre que estudiantes NO tienen falta
#print(tabulate(dt[(dt[2]==0) | (dt[3]==0) | (dt[4]==0)]))

#---Muestra que estudiantes tienen nota en más de 3.0
#dt[3] = pd.to_numeric(dt[5], errors='coerce')
#dt[4] = pd.to_numeric(dt[4], errors='coerce')
#dt[5] = pd.to_numeric(dt[3], errors='coerce')
#dt[6] = pd.to_numeric(dt[6], errors='coerce')
#print(tabulate(dt[(dt[3]>=3) & (dt[4]>=3) & (dt[5]>=3) & (dt[6]>=3)]))