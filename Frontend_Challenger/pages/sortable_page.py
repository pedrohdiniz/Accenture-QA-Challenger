from pages.base_page import BasePage
from pages.home_page import HomePage # Importar HomePage
from selenium.webdriver.common.by import By
import time

class SortablePage(BasePage):
    LIST_ITEMS = (By.CSS_SELECTOR, ".vertical-list-container .list-group-item")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.home_page = HomePage(self.driver)
    
    def navigate(self):
        self.home_page.load()
        self.home_page.click_card(self.home_page.CARD_INTERACTIONS)
        self.click_left_menu_item("Sortable")

    def get_current_list_order(self):
        items = self.find_elements(self.LIST_ITEMS)
        return [item.text for item in items]

    def sort_list_to_order(self, target_order):
        for index, target_text in enumerate(target_order):
            current_elements = self.find_elements(self.LIST_ITEMS)
            current_texts = self.get_current_list_order()
            
            if current_texts[index] == target_text:
                continue

            source_index = current_texts.index(target_text)
            source_element = current_elements[source_index]
            target_element = current_elements[index]
            
            self.actions.click_and_hold(source_element).move_to_element(target_element).release().perform()
            time.sleep(0.5)