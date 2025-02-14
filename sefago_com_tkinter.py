

import tkinter as tk  # Importa o módulo tkinter, que é usado para criar interfaces gráficas, e o renomeia para 'tk' para facilitar o uso.
from tkinter import messagebox  # Importa a classe messagebox do módulo tkinter, que fornece funções para exibir caixas de diálogo de mensagem, como avisos e erros.
from selenium import webdriver  # Importa a classe webdriver do Selenium, que é usada para controlar o navegador web de forma automatizada.
from selenium.webdriver.chrome.service import Service  # Importa a classe Service do módulo selenium.webdriver.chrome.service, usada para configurar o serviço do ChromeDriver.
from webdriver_manager.chrome import ChromeDriverManager  # Importa a classe ChromeDriverManager do módulo webdriver_manager.chrome, que gerencia automaticamente o download e a instalação do ChromeDriver.
from selenium.webdriver.common.by import By  # Importa a classe By do módulo selenium.webdriver.common.by, usada para localizar elementos na página web através de diferentes estratégias de busca (por exemplo, por ID, classe, XPath, etc.).
import threading  # Importa o módulo threading, que permite a execução de múltiplas threads (linhas de execução) simultaneamente, útil para evitar que a interface gráfica trave durante operações demoradas.
# Importa a função sleep da biblioteca time, usada para pausar a execução do script por um determinado tempo.
from time import sleep
def abrir_pagina():
    url = entry.get().strip()
    if not url:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira uma URL válida.")
        return

    if not (url.startswith("http://") or url.startswith("https://")):
        url = "https://" + url  # Adiciona https:// se o usuário não o tiver incluído

    try:
        # Configura o serviço do ChromeDriver
        service = Service(ChromeDriverManager().install())
        # Inicializa o driver do Chrome
        driver = webdriver.Chrome(service=service)
        # Maximiza a janela do navegador
        driver.maximize_window()
        # Abre a URL fornecida
        driver.get(url)
        print(f"Página {url} aberta com sucesso!")
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
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao abrir a página:\n{e}")

def on_button_click():
    # Usa threading para evitar que a interface gráfica trave enquanto o Selenium está executando
    threading.Thread(target=abrir_pagina).start()

# Cria a janela principal do Tkinter
root = tk.Tk()
root.title("Navegador Automatizado")

# Cria um rótulo para o campo de entrada
label = tk.Label(root, text="Digite a URL:")
label.pack(pady=10)

# Cria um campo de entrada para a URL
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Cria um botão para abrir a página
button = tk.Button(root, text="Abrir Página", command=on_button_click)
button.pack(pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()
