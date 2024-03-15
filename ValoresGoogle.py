from selenium import webdriver
import pyautogui as pgui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


navegador = webdriver.Chrome()
navegador.get('https://www.google.com')

def valorMoeda(moeda):
    campoBusca = navegador.find_element(By.NAME, 'q')
    campoBusca.clear()
    campoBusca.send_keys(moeda + ' hoje')
    campoBusca.send_keys(Keys.RETURN)

    try:
        elemento_valor = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'))
        )
        #print("Elemento não encontrado dentro do tempo para " + moeda)
        return elemento_valor.text  # Retorna o texto do elemento
      # Retorna o texto do elemento
    except TimeoutException:
        #print("Elemento não encontrado dentro do tempo para " + moeda)
        return "Não encontrado"

valorDolar = valorMoeda("Dolar")
valorEuro = valorMoeda("Euro")
valorLibras = valorMoeda("Libras")

print(f'O valor do dolar é: {valorDolar}')
print(f"O valor do euro é: {valorEuro}")
print(f"O valor do euro é: {valorLibras}")


