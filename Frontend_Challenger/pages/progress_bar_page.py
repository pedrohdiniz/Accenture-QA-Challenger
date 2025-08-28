from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from pages.home_page import HomePage
import time

class ProgressBarPage(BasePage):
    # Locators da página 
    START_STOP_BUTTON = (By.ID, "startStopButton")
    PROGRESS_BAR = (By.CSS_SELECTOR, "div[role='progressbar']")
    RESET_BUTTON = (By.ID, "resetButton")

    def __init__(self, driver):
        super().__init__(driver)
        self.home_page = HomePage(self.driver)

    def navigate(self):
        """Navega para a página Progress Bar a partir da home."""
        self.home_page.load()
        self.home_page.click_card(self.home_page.CARD_WIDGETS)
        self.click_left_menu_item("Progress Bar")

    def click_start_stop_button(self):
        self.click(self.START_STOP_BUTTON)

    def get_progress_value(self):
        try:
            value = self.get_attribute(self.PROGRESS_BAR, "aria-valuenow")
            return int(value)
        except (ValueError, TypeError):
            return 0

    def wait_for_progress_to_be_greater_than(self, target_value):
        start_time = time.time()
        timeout = 15
        while True:
            current_value = self.get_progress_value()
            if current_value > target_value:
                break 
            if time.time() - start_time > timeout:
                raise TimeoutException(f"A barra de progresso não ultrapassou o valor {target_value} em {timeout} segundos.")
            time.sleep(0.1)

    def wait_for_progress_to_reach(self, value):
        self.wait.until(
            EC.text_to_be_present_in_element_attribute(self.PROGRESS_BAR, "aria-valuenow", str(value))
        )
    
    def click_reset_button_when_visible(self):
        self.click(self.RESET_BUTTON)