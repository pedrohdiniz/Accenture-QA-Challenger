from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import os

def before_all(context):
    """
    Executado uma vez antes de todos os cenários.
    Configura o driver do Selenium de forma MANUAL.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    driver_path = os.path.join(project_root, 'chromedriver.exe')
    
    print(f"Tentando usar o chromedriver em: {driver_path}") 
    service = ChromeService(executable_path=driver_path)
    
    context.driver = webdriver.Chrome(service=service, options=options)
    context.resources_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources')

def after_all(context):
    """
    Executado uma vez após todos os cenários.
    Fecha o navegador.
    """
    if hasattr(context, 'driver'):
        context.driver.quit()
