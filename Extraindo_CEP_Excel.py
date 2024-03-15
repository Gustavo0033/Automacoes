from selenium import webdriver as WB
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as pgui
import xlsxwriter
import subprocess
from openpyxl import load_workbook




navegador = WB.Chrome()
navegador.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

navegador.find_element(By.ID, 'endereco').send_keys('03040000')
navegador.find_element(By.ID, 'endereco').send_keys(Keys.RETURN)
pgui.sleep(2)

rua = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
print(rua)

bairro = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
print(bairro)

cidade = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
print(cidade)

cep = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text
print(cep)

navegador.quit()

#---------------------- MOSTRAR NO EXCEL ----------------------------


#5 imporimti a linha a2 e transformar em string

#procura o caminho do arquivo
nomeArquivo = '/Users/gustavomendonca/Documents/CEPs/CEP.xlsx'

#abre o arquivo para edicao ou leitura
planilhaDados = load_workbook(nomeArquivo)

#seleciona a aba Dados
sheetDados = planilhaDados['Dados']
#seleciona a aba Dados
sheetCEP = planilhaDados['CEPs']

#pegamos a linha A da planilha e adicionaremos os dados abaixo dela
#sempre colocando abaixo
linha = len(sheetDados['A']) + 1

#imprimirá na A2 e transformou linha em uma string
colunaA = 'A' + str(linha) #imprimirá na A2
colunaB = 'B' + str(linha) #imprimirá na B2
colunaC = 'C' + str(linha) #imprimirá na C2

#salvando rua, bairor e cidade na aba Dados
sheetDados[colunaA] = rua
sheetDados[colunaB] = bairro
sheetDados[colunaC] = cidade

#salvando cep na aba CEP
sheetCEP[colunaA] = cep

#salvando o arquivo
planilhaDados.save(filename=nomeArquivo)

#abrindo o arquivo
subprocess.run(['open', nomeArquivo])
