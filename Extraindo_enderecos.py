from selenium import webdriver as WB
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as pgui

#1 abrir o navegador
#2 pegar o elemento onde vamos pesquisar o endereco
#3 colocar o cep no campo de texto de pesquisa
#4 pegar o endereco, bairro, uf e cep


navegador = WB.Chrome()
navegador.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
pgui.sleep(3)



navegador.find_element(By.ID, 'endereco').send_keys('03040000')
navegador.find_element(By.ID, 'endereco').send_keys(Keys.RETURN)
pgui.sleep(3)



rua = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
print(rua)

bairro = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
print(bairro)

cidade = navegador.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
print(cidade)


