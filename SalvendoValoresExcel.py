from selenium import webdriver
import pyautogui as pgui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import xlsxwriter
import subprocess
# ------------------------------ PESQUISANDO E IMPRIMINDO VALOR DOLAR, EURO E LIBRA -----------------
navegador = webdriver.Chrome()
navegador.get('https://www.google.com')

def buscarValorMoeda(moeda):
   campoBusca = navegador.find_element(By.NAME, 'q')
   campoBusca.clear()
   campoBusca.send_keys(moeda + ' hoje')
   campoBusca.send_keys(Keys.RETURN)

   try:
       elementoValor = WebDriverWait(navegador, 10).until(
           EC.presence_of_element_located((By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'))
       )
       return elementoValor.text
   except TimeoutException:
       return 'Valor não encontrado.'


valorDolar = buscarValorMoeda('Dolar')
valorEuro = buscarValorMoeda('Euro')
valorLibras = buscarValorMoeda('Libras')

print(valorDolar)
print(valorEuro)
print(valorLibras)

navegador.quit()

#--------------------------- MOSTRAR NO EXCEL ---------------------------


nomeArquivo = '/Users/gustavomendonca/Documents/Excel/valoresGoogle.xlsx'
planilhaAberta = xlsxwriter.Workbook(nomeArquivo)
planilha = planilhaAberta.add_worksheet()

planilha.write('A1','Moeda')
planilha.write('B1','Valor em real')
planilha.write('A2', 'Dólar')
planilha.write('B2', valorDolar)
planilha.write('A3', 'Euro')
planilha.write('B3', valorEuro)
planilha.write('A4', 'Libras')
planilha.write('B4', valorLibras)

planilhaAberta.close()



subprocess.run(['open', nomeArquivo])











