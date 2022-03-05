#planilha_dataframe.py
#Dataframe é um objeto da biblioteca pandas

import xlsxwriter
import os
import pandas as pd

#Cria um dicionário usando um Dataframe para preencher as informações da planilha
dataFrame = pd.DataFrame ({'Nome'   : ['João', 'Verônica','Sabrina','Noemi'],
                           'Idade'  : [30,25,33,19],
                           'Salario': [3000,4500,2900,5500]
                          })



#Cria e salva a planilha usando o pd.ExcelWriter
arquivo = pd.ExcelWriter('quarto_arquivo.xlsx', engine ='xlsxwriter')

#Converte o dataframe em um objeto Excel
dataFrame.to_excel(arquivo,sheet_name='Dados')

#Pega a pasta de trabalho xlsxwriter (workbook) e os objetos da planilha.
workbook = arquivo.book
worksheet = arquivo.sheets['Dados']


#Variável para colocar formato da moeda
formatoMoeda = workbook.add_format({'num_format':'#,##0.00'})

#Adiciona formato da moeda na coluna
worksheet.set_column('D:D',None,formatoMoeda)


workbook.close()
os.startfile(arquivo)
