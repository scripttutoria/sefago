# Importa a classe webdriver do Selenium, que é usada para controlar o navegador.
from selenium import webdriver
# Importa ChromeDriverManager do webdriver_manager, que gerencia automaticamente o download e a instalação do ChromeDriver.
from webdriver_manager.chrome import ChromeDriverManager
# Importa a classe Service do Selenium, usada para configurar o serviço do ChromeDriver.
from selenium.webdriver.chrome.service import Service
# Importa a classe By do Selenium, usada para localizar elementos na página.
from selenium.webdriver.common.by import By
# Importa a função sleep da biblioteca time, usada para pausar a execução do script por um determinado tempo.
from time import sleep
# Configura o serviço do ChromeDriver usando o ChromeDriverManager para instalar automaticamente a versão correta do driver.
service = Service(ChromeDriverManager().install())
# Inicializa o driver do Chrome com o serviço configurado acima.
driver = webdriver.Chrome(service=service)

try:
    # Maximiza a janela do navegador (opcional, se já foi usado --start-maximized)
    driver.maximize_window()
    # Abre a página web desejada
    driver.get("https://goias.gov.br/economia/documentos-fiscais/")
    # Aguarda 5 segundos para garantir que a página carregue completamente. O uso de sleep é uma forma simples de esperar, mas em projetos mais avançados, considere usar esperas explícitas ou implícitas
    sleep(5)
    
    print("Página aberta com sucesso!")
    # Realiza scroll para uma posição específica (por exemplo, 500 pixels abaixo)
    driver.execute_script("window.scrollTo(0, 500);")
    # Imprime uma mensagem indicando que a página foi aberta com sucesso.
    print("Scroll realizado para 500 pixels abaixo.")
    sleep(2)
    # Localiza um elemento na página usando um seletor CSS. O seletor '.g-title+ .nomargintop li:nth-child(3) a' busca um link que é o terceiro filho de um elemento li que segue imediatamente um elemento com a classe 'g-title' e tem a classe 'nomargintop'.
    elemento = driver.find_element(By.CSS_SELECTOR, '.g-title+ .nomargintop li:nth-child(3) a')
    sleep(5)
    elemento.click()
    print("Elemento clicado com sucesso!")
    # Aguarda que o usuário pressione Enter antes de continuar. Isso é útil para depuração, permitindo que você veja o resultado antes de o navegador fechar.
    input()

finally:
    # Fecha o navegador após a execução do bloco try, independentemente de ter ocorrido uma exceção.
    driver.quit()
