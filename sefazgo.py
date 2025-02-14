from selenium import webdriver  # Importa a classe webdriver do Selenium, que é usada para controlar o navegador.
from webdriver_manager.chrome import ChromeDriverManager  # Importa ChromeDriverManager do webdriver_manager, que gerencia automaticamente o download e a instalação do ChromeDriver.
from selenium.webdriver.chrome.service import Service  # Importa a classe Service do Selenium, usada para configurar o serviço do ChromeDriver.
from selenium.webdriver.common.by import By  # Importa a classe By do Selenium, usada para localizar elementos na página.
from time import sleep  # Importa a função sleep da biblioteca time, usada para pausar a execução do script por um determinado tempo.

# Configura o serviço do ChromeDriver usando o ChromeDriverManager para instalar automaticamente a versão correta do driver.
service = Service(ChromeDriverManager().install())

# Inicializa o driver do Chrome com o serviço configurado acima.
driver = webdriver.Chrome(service=service)

try:
    # Maximiza a janela do navegador. Isso é opcional e pode ser redundante se a opção --start-maximized for usada.
    driver.maximize_window()

    # Abre a página web desejada. Atualmente, está vazio; você deve substituir "" pela URL desejada, por exemplo, "https://www.example.com".
    driver.get("")

    # Aguarda 5 segundos para garantir que a página carregue completamente. O uso de sleep é uma forma simples de esperar, mas em projetos mais avançados, considere usar esperas explícitas ou implícitas.
    sleep(5)

    # Imprime uma mensagem indicando que a página foi aberta com sucesso.
    print("Página aberta com sucesso!")

    # Realiza scroll para uma posição específica na página, neste caso, 500 pixels abaixo do topo.
    driver.execute_script("window.scrollTo(0, 500);")

    # Imprime uma mensagem indicando que o scroll foi realizado.
    print("Scroll realizado para 500 pixels abaixo.")

    # Aguarda 2 segundos para garantir que o scroll seja concluído.
    sleep(2)

    # Localiza um elemento na página usando um seletor CSS. O seletor '.g-title+ .nomargintop li:nth-child(3) a' busca um link que é o terceiro filho de um elemento li que segue imediatamente um elemento com a classe 'g-title' e tem a classe 'nomargintop'.
    elemento = driver.find_element(By.CSS_SELECTOR, '.g-title+ .nomargintop li:nth-child(3) a')

    # Aguarda mais 5 segundos para garantir que o elemento esteja interagível. Isso pode ser necessário se o elemento ainda estiver carregando ou se houver animações.
    sleep(5)

    # Clica no elemento localizado.
    elemento.click()

    # Imprime uma mensagem indicando que o elemento foi clicado com sucesso.
    print("Elemento clicado com sucesso!")

    # Aguarda que o usuário pressione Enter antes de continuar. Isso é útil para depuração, permitindo que você veja o resultado antes de o navegador fechar.
    input()

finally:
    # Fecha o navegador após a execução do bloco try, independentemente de ter ocorrido uma exceção.
    driver.quit()
