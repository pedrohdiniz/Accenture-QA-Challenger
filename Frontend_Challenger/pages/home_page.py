from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://demoqa.com/"
    
    # Locators para os cards da página inicial
    CARD_ELEMENTS = (By.XPATH, "//h5[text()='Elements']")
    CARD_FORMS = (By.XPATH, "//h5[text()='Forms']")
    CARD_ALERTS = (By.XPATH, "//h5[text()='Alerts, Frame & Windows']")
    CARD_WIDGETS = (By.XPATH, "//h5[text()='Widgets']")
    CARD_INTERACTIONS = (By.XPATH, "//h5[text()='Interactions']")

    def load(self):
        self.go_to_url(self.URL)

    def click_card(self, card_locator):
        """Clica em um card específico na página inicial."""
        self.scroll_to_element(card_locator)
        self.click(card_locator)