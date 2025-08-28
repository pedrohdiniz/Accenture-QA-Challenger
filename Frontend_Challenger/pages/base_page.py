from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By # Importar By
import time

class BasePage:
    """
    Classe base para todas as Pages. Contém métodos de interação genéricos com os elementos.
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15, ignored_exceptions=[ElementClickInterceptedException, StaleElementReferenceException])
        self.actions = ActionChains(self.driver)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        
    def get_text(self, locator):
        return self.find_element(locator).text

    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)
    
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        time.sleep(0.5)

    def click_left_menu_item(self, item_text):
        """
        Clica em um item no menu de navegação esquerdo, encontrando-o pelo texto.
        """
        locator = (By.XPATH, f"//li[contains(@class, 'btn-light')][span[text()='{item_text}']]")
        self.scroll_to_element(locator)
        self.click(locator)