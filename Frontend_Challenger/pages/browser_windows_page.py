from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.home_page import HomePage
import time 

class BrowserWindowsPage(BasePage):
    # Locators.
    NEW_WINDOW_BUTTON = (By.ID, "windowButton")
    SAMPLE_PAGE_HEADING = (By.ID, "sampleHeading")

    def __init__(self, driver):
        super().__init__(driver)
        self.home_page = HomePage(self.driver)
        # Esta variável vai guardar o identificador da janela original.
        self.original_window_handle = None

    def navigate(self):
        """Navega para a página Browser Windows a partir da home."""
        self.home_page.load()
        # Guardar o identificador da janela atual (a principal).
        self.original_window_handle = self.driver.current_window_handle        
        self.home_page.click_card(self.home_page.CARD_ALERTS)
        self.click_left_menu_item("Browser Windows")
          
    def click_new_window(self):
        """Clica no botão que abre a nova janela."""
        self.click(self.NEW_WINDOW_BUTTON)

    def switch_to_new_window(self):
        """
        Muda o foco do Selenium da janela original para a janela recém-aberta.
        """        
        time.sleep(1) 
        
        # Lista de todas as janelas abertas no momento.
        open_windows = self.driver.window_handles
        
        # Percorrer essa lista para encontrar a janela nova.
        for window in open_windows:
            # A nova janela é aquela cujo identificador é DIFERENTE do identificador da janela original que guardamos.
            if window != self.original_window_handle:                
                self.driver.switch_to.window(window)                
                break

    def get_new_window_message(self):
        """Pega o texto que está dentro da nova janela."""        
        return self.get_text(self.SAMPLE_PAGE_HEADING)

    def close_new_window_and_switch_back(self):
        """Fecha a janela atual (a nova) e devolve o foco para a janela original."""       
        self.driver.close()
        self.driver.switch_to.window(self.original_window_handle)