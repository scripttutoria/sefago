from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Maximiza a janela do navegador (opcional, se já foi usado --start-maximized)
    driver.maximize_window()
    driver.get("https://goias.gov.br/economia/documentos-fiscais/")
    sleep(5)
    print("Página aberta com sucesso!")
    # Realiza scroll para uma posição específica (por exemplo, 500 pixels abaixo)
    driver.execute_script("window.scrollTo(0, 500);")
    print("Scroll realizado para 500 pixels abaixo.")
    sleep(2)
    elemento = driver.find_element(By.CSS_SELECTOR, '.g-title+ .nomargintop li:nth-child(3) a')
    sleep(5)
    elemento.click()
    print("Elemento clicado com sucesso!")
    input()

finally:
    driver.quit()
