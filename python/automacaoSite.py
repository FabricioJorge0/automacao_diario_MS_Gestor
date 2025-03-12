'''from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://msgestor.msconnect.com.br/pages/auth/login")
sleep(5)

campo_usuario = driver.find_element(By.XPATH,"//input[@id='mat-input-26']")
campo_senha = driver.find_element(By.XPATH,"//input[@id='mat-input-27']")
#campo_botao = driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator submit-button ng-tns-c260-103 mat-raised-button mat-button-base mat-accent']")

campo_usuario.send_keys('allef.sousa')
campo_senha.send_keys('98638C3')
campo_senha.send_keys(Keys.RETURN)
#campo_botao.click()

input("")'''

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v131.fed_cm import click_dialog_button
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

def login_site(url, usuario, senha):
    """
    Realiza o login em um site usando Selenium.

    Args:
        url (str): O URL do site.
        usuario (str): O nome de usuário.
        senha (str): A senha.
    """

    # Inicializa o navegador (exemplo: Chrome)
    caminho_chromedriver = "C:\\Users\\06010940184\\automacao_diario_MS_Gestor\\python\\ChromeDriver\\chromedriver-win64\\chromedriver.exe"  # windows


    servico = Service(caminho_chromedriver)
    driver = webdriver.Chrome(service=servico)

    try:
        # Abre o site
        driver.get(url)

        # Encontra os campos de usuário e senha e preenche
        campo_usuario = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mat-input-26"))  # Substitua "username" pelo ID correto
        )
        campo_senha = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mat-input-27"))  # Substitua "password" pelo ID correto
        )

        campo_usuario.send_keys(usuario)
        campo_senha.send_keys(senha)

        # Encontra e clica no botão de login

        sleep(3)
        campo_senha.send_keys(Keys.RETURN)

        '''campoBotao = driver.find_element(By.XPATH, "//mat-icon[@class='mat-icon notranslate material-icons mat-icon-no-color']")
        campoBotao.click()'''


        '''botao_config = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mat-focus-indicator mat-icon-button mat-button-base btnSettings mat-elevation-z4 theme-options-button ng-star-inserted side-panel-hidden"))  # Substitua "login-button" pelo ID correto
        )
        botao_config.send_keys(Keys.RETURN)'''

        # Aguarda a página de login ser carregada (opcional)
        '''WebDriverWait(driver, 10).until(
            EC.url_changes(url)  # Aguarda a URL mudar após o login
        )'''

        print("Login realizado com sucesso!")

    except Exception as e:
        print(f"Erro durante o login: {e}")

    finally:
        # Mantém o navegador aberto após o login (remova se quiser fechar automaticamente)
        input("Pressione Enter para fechar o navegador...")
        driver.quit()

# Exemplo de uso
url_do_site = "https://msgestor.msconnect.com.br/pages/auth/login"  # Substitua pelo URL do site
nome_de_usuario = "allef.sousa"  # Substitua pelo seu nome de usuário
senha_de_acesso = "98638C3"  # Substitua pela sua senha

login_site(url_do_site, nome_de_usuario, senha_de_acesso)