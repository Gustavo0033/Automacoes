import xlsxwriter
import subprocess


nomeArquivo = "/Users/gustavomendonca/Documents/Excel/Contatos.xlsx"
planilhaCriada = xlsxwriter.Workbook(nomeArquivo)
planilha = planilhaCriada.add_worksheet()

planilha.write('A1', 'Nome')
planilha.write('A2', "Gustavo")

planilhaCriada.close()

subprocess.run(['open', nomeArquivo])