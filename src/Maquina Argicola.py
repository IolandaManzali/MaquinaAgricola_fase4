
#-----Valores/Variáveis-----
# Cada Dia representa um conjunto de valores que seriam lidos a cada dia como se foçe na vida real, lembrando que esses 5 blocos são apenas uma parte dos dados presentes no banco 

#-----PROGRAMA PRINCIPÁL
import pyodbc
import time

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-FQOLT90;"
    "Database=AGRO;"
)
conexao = pyodbc.connect(dados_conexao)
print('Conexao Bem Sucedida')

cursor = conexao.cursor()

# Obtendo os nomes das colunas
cursor.execute("SELECT * FROM dadosagrotest")
colunas = [column[0] for column in cursor.description]

# Executando a consulta novamente para obter os dados
cursor.execute("SELECT * FROM dadosagrotest")
rows = cursor.fetchall()

# Imprimindo os resultados com os nomes das colunas
for row in rows:
    for i, valor in enumerate(row):
        print(f"{colunas[i]}: {valor}")

print('Os dados criados para o banco são ficticos e serão utilizados dados aleatórios para fins de teste,com objetivo de fins academicos!')

time.sleep(7)
# Dia 1
print("----Dia 1----")
print("---Umidade---")
umidade1 =  60
if umidade1 < 50:
  print("A umidade está abaixo do necessário, ligue a bomba")    
elif umidade1 >= 51 and umidade1 <=75:
  print("A umidade está ideal, bomba desligada")
else:
  print("A umidade está acima do necessário, bomba desligada")
print("---PH---")
ph1 =  7
if ph1 >= 1 and ph1 < 7:
  print("Nivél de PH Ácido ")
elif ph1 == 7:
  print("Nível de PH Neutro")
elif ph1 > 7 and ph1 <= 14:
   print("Nível de Ph Básico")
else: 
  print("Valor Inválido")
print("---Fosforo---")
fosforo1 = 42
if fosforo1 > 20 and fosforo1 < 45:
  print ("True, não precisa de nenhum tipo de correção")
else:
   print ("False, precisa de algum tipo de coreção")
print("---Potassio---")
potassio1 =  43
if potassio1 > 20 and potassio1 < 45:
  print ("True, não precisa de nenhum tipo de correção")
else:
  print ("False, precisa de algum tipo de coreção")

  # Dia 2
print("----Dia 2----")
print("---Umidade---")
umidade2 =  70
if umidade2 < 50:
  print("A umidade está abaixo do necessário, ligue a bomba")
elif umidade2 >= 51 and umidade2 <=75:
   print("A umidade está ideal, bomba desligada")
else:
  print("A umidade está acima do necessário, bomba a desligada")
print("---PH---")
ph2 =  11.5
if ph2 >= 1 and ph2 < 7:
   print("Nivél de PH Ácido ")
elif ph2 == 7:
   print("Nível de PH Neutro")
elif ph2 > 7 and ph2 <= 14:
   print("Nível de Ph Básico")
else: 
   print("Valor Inválido")
print("---Fosforo---")
fosforo2 = 58
if fosforo2 > 20 and fosforo2 < 45:
   print ("True, não precisa de nenhum tipo de correção")
else:
   print ("False, precisa de algum tipo de coreção")
print("---Potassio---")
potassio2 =  41
if potassio2 > 20 and potassio2 < 45:
   print ("True, não precisa de nenhum tipo de correção")
else:
   print ("False, precisa de algum tipo de coreção")

# Dia 3
print("----Dia 3----")
print("---Umidade---")
umidade3 =  55.59
if umidade3 < 50:
   print("A umidade está abaixo do necessário, ligue a bomba")   
elif umidade3 >= 51 and umidade3 <=75:
   print("A umidade está ideal, bomba desligada")
else:
   print("A umidade está acima do necessário, bomba a desligada")
print("---PH---")
ph3 =  3.5
if ph3 >= 1 and ph3 < 7:
   print("Nivél de PH Ácido ")
elif ph3 == 7:
   print("Nível de PH Neutro")
elif ph3 > 7 and ph3 <= 14:
   print("Nível de Ph Básico")
else: 
   print("Valor Inválido")
print("---Fosforo---")
fosforo3 = 55
if fosforo3 > 20 and fosforo3 < 45:
   print ("True, não precisa de nenhum tipo de correção")
else:
   print ("False, precisa de algum tipo de coreção")
print("---Potassio---")
potassio3 =  44
if potassio3 > 20 and potassio3 < 45:
   print ("True, não precisa de nenhum tipo de correção")
else:
   print ("False, precisa de algum tipo de coreção")

# Dia 4
print("----Dia 4----")
print("---Umidade---")
umidade4 =  78.9
if umidade4 < 50:
   print("A umidade está abaixo do necessário, ligue a bomba")   
elif umidade4 >= 51 and umidade4 <=75:
   print("A umidade está ideal, bomba desligada")
else:
   print("A umidade está acima do necessário, bomba a desligada")
print("---PH---")
ph4 =  4.5
if ph4 >= 1 and ph4 < 7:
   print("Nivél de PH Ácido ")
elif ph4 == 7:
   print("Nível de PH Neutro")
elif ph4 > 7 and ph4 <= 14:
    print("Nível de Ph Básico")
else: 
    print("Valor Inválido")
print("---Fosforo---")
fosforo4 = 35
if fosforo4 > 20 and fosforo4 < 45:
   print ("True, não precisa de nenhum tipo de correção")
else:
   print ("False, precisa de algum tipo de coreção")
print("---Potassio---")
potassio4 =  40
if potassio4 > 20 and potassio4 < 45:
   print ("True, não precisa de nenhum tipo de correção")
else:
   print ("False, precisa de algum tipo de coreção")
   # Dia 5
print("----Dia 5----")
print("---Umidade---")
umidade5 = 42.89
if umidade5 < 50:
   print("A umidade está abaixo do necessário, ligue a bomba")   
elif umidade5 >= 51 and umidade5 <=75:
   print("A umidade está ideal, bomba desligada")
else:
   print("A umidade está acima do necessário, bomba a desligada")
print("---PH---")
ph5 = 11
if ph5 >= 1 and ph5 < 7:
   print("Nivél de PH Ácido ")
elif ph5 == 7:
   print("Nível de PH Neutro")
elif ph5 > 7 and ph5 <= 14:
   print("Nível de Ph Básico")
else: 
    print("Valor Inválido")
print("---Fosforo---")
fosforo5 = 42
if fosforo5 > 20 and fosforo5 < 45:
   print ("True, não precisa de nenhum tipo de correção")
else:
   print ("False, precisa de algum tipo de coreção")
print("---Potassio---")
potassio5 =  20
if potassio5 > 25 and potassio5 < 45:
   print ("True, não precisa de nenhum tipo de correção")
else:
   print ("False, precisa de algum tipo de coreção")