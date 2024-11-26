import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

var_service = Service(ChromeDriverManager().install()) # aways install recent version of webdriver Chrome
navegator = webdriver.Chrome(service = var_service)

navegator.get('https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M')
navegator.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys('Martim Tiburcio')
navegator.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys('tiburcio.contato@gmail.com')
navegator.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button').click()
time.sleep(3)
navegator.find_element('xpath', '//*[@id="popup-container"]/div/div/a[2]').click()

detail = '-' * 10
input(f'\n{detail}[ Para encerrar pressione enter ]{detail}\n\n')
print('Encerrando')
time.sleep(3)