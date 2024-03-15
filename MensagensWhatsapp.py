from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as pgui
import pyautogui as teclasTeclado
from openpyxl import load_workbook


nomeArquivo = '/Users/gustavomendonca/Documents/Whatsapp_Python/wpp_python.xlsx'
carregarArquivo = load_workbook(nomeArquivo)
abaSelecionada = carregarArquivo['Contatos']

navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')

while len(navegador.find_elements(By.ID, 'side')) < 1:
    pgui.sleep(2)

pgui.sleep(3)


for linha in range(2, len(abaSelecionada['A'])+ 1):
    nomeContato = abaSelecionada['A%s' % linha].value
    mensagemContato = abaSelecionada['B%s' % linha].value

    navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(nomeContato)
    pgui.sleep(1)
    teclasTeclado.press('enter')
    pgui.sleep(2)

    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(mensagemContato)
    pgui.sleep(2)
    teclasTeclado.press('enter')
    pgui.sleep(3)

