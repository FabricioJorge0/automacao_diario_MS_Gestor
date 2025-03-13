from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard

driver = webdriver.Chrome()


def acao_site(elemento):
    # Localiza a aba desejada para preenchimento da data e gera um click
    campo_expandir = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, elemento))
    )
    campo_expandir.click()


try:
    # localiza a endereço e entrar no site MSGestor
    driver.get("https://msgestor.msconnect.com.br/pages/auth/login")
    sleep(2)

    # Localiza os campos de login Usuário e senha
    campo_usuario = driver.find_element(By.XPATH, "//input[@id='mat-input-26']")
    campo_senha = driver.find_element(By.XPATH, "//input[@id='mat-input-27']")
    sleep(1)
    # Preencge os campos de login usuário e senha
    campo_usuario.send_keys('allef.sousa')
    campo_senha.send_keys('98638C3')
    sleep(1)
    # Gera um click no ENTER para realizar o Login
    campo_senha.send_keys(Keys.RETURN)

    sleep(5)
except Exception as e:
    print(f"Erro durante o login: {e}")

try:
    acao_site("//button[contains(@class, 'btnSettings')]")

    '''#Localiza o botão de configurações e gera um click
    campo_botao = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'btnSettings')]"))


    )
    campo_botao.click()'''
except Exception as e:
    print("Erro ao encontrar o botão:", e)

try:
    acao_site("//mat-expansion-panel-header[@id='mat-expansion-panel-header-16']")

    '''#Localiza a aba desejada para preenchimento da data e gera um click
    campo_expandir = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//mat-expansion-panel-header[@id='mat-expansion-panel-header-16']"))
    )
    campo_expandir.click()'''
except Exception as e:
    print("Erro ao encontrar ou expandir aba:", e)

try:

    # Localiza os campos de data
    campo_data_inicio = driver.find_element(By.XPATH, "//input[@id='mat-input-28']")
    campo_data_final = driver.find_element(By.XPATH, "//input[@id='mat-input-29']")

    # Aguarda o campo de data e abre o calendário
    campo_data_inicio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mat-input-28"))
    )
    campo_data_inicio.click()

    # Cria uma div na página com uma mensagem para preencher as datas desejadas
    driver.execute_script("""
        var popup = document.createElement('div');
        popup.style.position = 'fixed';
        popup.style.top = '50%';
        popup.style.left = '30%';
        popup.style.transform = 'translate(-50%, -50%)';
        popup.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
        popup.style.color = 'white';
        popup.style.padding = '20px';
        popup.style.borderRadius = '10px';
        popup.style.fontSize = '18px';
        popup.style.zIndex = '9999';  // Definindo um z-index alto para garantir que o popup fique à frente
        popup.innerHTML = 'Selecione a data manualmente e clique em OK para continuar.';
        popup.id = 'popupAlert';

        var button = document.createElement('button');
        button.innerText = 'OK';
        button.style.marginTop = '10px';
        button.style.backgroundColor = '#4CAF50';
        button.style.color = 'white';
        button.style.padding = '10px 20px';
        button.style.border = 'none';
        button.style.borderRadius = '5px';
        button.style.cursor = 'pointer';
        button.onclick = function() {
            popup.remove();
        };

        popup.appendChild(button);
        document.body.appendChild(popup);
    """)

    # A automação pode continuar sem ser bloqueada, você pode interagir com o site normalmente
    print("O popup foi exibido. Agora você pode preencher a data manualmente.")

    # Aguarda a remoção do popup (ou até você clicar em OK)
    WebDriverWait(driver, 300).until(
        EC.invisibility_of_element_located((By.ID, "popupAlert"))
    )

    # Após você clicar em OK no popup, a automação continua
    print("Automação retomada após a seleção da data.")

    # Após o popup sair será gerado um click no botão "Aplicar e salvar filtros"
    campo_expandir = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//button[@class='mat-focus-indicator ng-tns-c233-107 mat-raised-button mat-button-base mat-accent']"))
    )
    campo_expandir.click()


except Exception as e:
    print(f"Erro durante ao preencher campos de datas: {e}")

try:

    campo_download = driver.find_element(By.XPATH, "//div[@id='mat-select-value-97']")

    # Aguarda o campo de data e abre o calendário
    campo_data_inicio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mat-select-value-97"))
    )
    campo_download.click()
    sleep(5)




except Exception as e:
    print(f"Erro ao expandir área de download: {e}")

finally:
    input("Pressione Enter para fechar o navegador...")
    driver.quit()
