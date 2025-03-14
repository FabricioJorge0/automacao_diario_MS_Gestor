from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


download_dir = "M:\\ADM DE VENDAS PJ\\Diario Imput\\testeDeDownload"
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Para abrir o navegador maximizado

prefs = {
    "download.default_directory": download_dir,  # Diretório de download
    "download.prompt_for_download": False,  # Desativa o prompt de confirmação de download
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True  # Habilita a navegação segura (impede mensagens de segurança)
}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)

#função para diminuir o código
def acao_site(elemento):

    #codigo para expendir o campo para buscar data
    campo_expandir = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, elemento))
    )
    campo_expandir.click()

def expandir_painel(xpath, path):

    #encontra o painel de expansão de download e gera um click para expandir
    campo_download = driver.find_element(By.XPATH, xpath)

    # Aguarda o campo de data e abre o calendário
    campo_download = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, path))
    )
    campo_download.click()

def downloadArquivos(xpath, path):
    download_1 = driver.find_element(By.XPATH, xpath)
    download_1 = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, path))
    )
    download_1.click()
    sleep(1)

try:
    #localiza a endereço e entrar no site MSGestor
    driver.get("https://msgestor.msconnect.com.br/pages/auth/login")
    sleep(2)

    #Localiza os campos de login Usuário e senha
    campo_usuario = driver.find_element(By.XPATH,"//input[@id='mat-input-26']")
    campo_senha = driver.find_element(By.XPATH,"//input[@id='mat-input-27']")
    sleep(1)
    #Preencge os campos de login usuário e senha
    campo_usuario.send_keys('allef.sousa')
    campo_senha.send_keys('98638C3')
    sleep(1)
    #Gera um click no ENTER para realizar o Login
    campo_senha.send_keys(Keys.RETURN)

    sleep(5)
except Exception as e:
    print(f"Erro durante o login: {e}")


try:
    sleep(1)
    #localiza o botão de configuração e gera um click
    acao_site("//button[contains(@class, 'btnSettings')]")

except Exception as e:
    print("Erro ao encontrar o botão:", e)



try:
    #localiza o painel de expanção para pesquisar a data e expande
    acao_site("//mat-expansion-panel-header[@id='mat-expansion-panel-header-16']")

except Exception as e:
    print("Erro ao encontrar ou expandir aba:", e)


#Aqui irá encontrar os campos de data, criar um modal para pausar a aplicação para preenchimento manual das datas
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
    sleep(1)
    acao_site("//button[@class='mat-focus-indicator ng-tns-c233-107 mat-raised-button mat-button-base mat-accent']")

except Exception as e:
    print(f"Erro durante ao preencher campos de datas: {e}")

sleep(15)

try:
    expandir_painel("//div[@id='mat-select-value-97']", "mat-select-value-97")
    sleep(2)
    downloadArquivos("//mat-option[@id='mat-option-227']", 'mat-option-227')
    sleep(5)


except Exception as e:
    print(f"Erro ao fazer download: {e}")


elemento = driver.find_element(By.XPATH, '//div[@id="mat-select-value-95"]')  # Insira o XPATH correto do elemento
# Realiza o scroll até o elemento
driver.execute_script("arguments[0].scrollIntoView();", elemento)

try:
    expandir_painel("//div[@id='mat-select-value-95']", "mat-select-value-95")
    sleep(2)
    downloadArquivos("//mat-option[@id='mat-option-224']", "mat-option-224")

except Exception as e:
    print(f"Erro ao expandir área de download: {e}")

sleep(3)

try:
    #downloadArquivos("//mat-option[@id='mat-option mat-focus-indicator ng-tns-c130-220']", "mat-option-221")

    expandirElemento = driver.find_element(By.ID, "mat-select-value-93")
    # Força o clique com JavaScript
    driver.execute_script("arguments[0].click();", expandirElemento)

    sleep(2)
    fazerDownload = driver.find_element(By.XPATH, "//mat-option[@value='detalhamento-msgestor']")
    fazerDownload.click()







except Exception as e:
    print(f"Erro ao expandir área de download: {e}")
finally:
    input("Pressione Enter para fechar o navegador...")
    driver.quit()










