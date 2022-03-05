#primeira_planilha.py
#https://xlsxwriter.readthedocs.io site com documentação da biblioteca
#pip install xlsxwriter

import xlsxwriter
import os

caminhoArquivo = "primeiro_arquivo.xlsx"

workbook = xlsxwriter.Workbook(caminhoArquivo)

#cria uma nova sheet em branco com o nome de Sheet1
worksheet = workbook.add_worksheet()

#adicona dados no worksheet
worksheet.write('A1','Nome')
worksheet.write('B1', 'Idade')
worksheet.write('A2','João da Silva')
worksheet.write('B2','33')
worksheet.write('A3','Maria da Silva')
worksheet.write('B3','32')

#fecha arquivo
workbook.close()


#abrir planilha
os.startfile(caminhoArquivo)

