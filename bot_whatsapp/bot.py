from typing import KeysView
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configurações do WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Executar o navegador em modo headless (sem interface gráfica)
driver = webdriver.Chrome("https://web.whatsapp.com/", options=chrome_options)  # Substitua pelo caminho do seu WebDriver

def welcome_new_member(group_name, member_name):
    message = f"Bem-vindo(a), {member_name} ao grupo {group_name}!"
    input_box = driver.find_element_by_xpath("//div[@contenteditable='true']")
    input_box.send_keys(message)
    input_box.send_keys(KeysView.RETURN)

# Exemplo de uso
group_name = "Nome do grupo"
new_member_name = "Nome do novo membro"
welcome_new_member(group_name, new_member_name)