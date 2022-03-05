#planilha_propriedades.py

import xlsxwriter
import os
import datetime

caminhoArquivo = "segundo_arquivo.xlsx"

workbook = xlsxwriter.Workbook(caminhoArquivo)

#propriedades da planilha
workbook.set_properties({
    'category' : 'Estudante',
    'title' : 'Arquivo do Excel criado com python',
    'subject' : 'Aula Python Excel',
    'author' : 'Gustavo Simões',
    'company': 'Makita',
    'create' : datetime.date(2022,3,5),
    'comments' : 'Bem vindo ao Python para Excel'
})


#cria uma nova sheet em branco com o nome de Sheet1
worksheet = workbook.add_worksheet('Dados')

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
