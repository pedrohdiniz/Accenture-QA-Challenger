from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.home_page import HomePage
from faker import Faker

class PracticeFormPage(BasePage):
    URL = "https://demoqa.com/automation-practice-form"
    
    # Locators
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    GENDER_MALE_RADIO = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    MOBILE_INPUT = (By.ID, "userNumber")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    UPLOAD_PICTURE_BTN = (By.ID, "uploadPicture")
    STATE_DROPDOWN = (By.ID, "state")
    STATE_INPUT = (By.ID, "react-select-3-input")
    CITY_DROPDOWN = (By.ID, "city")
    CITY_INPUT = (By.ID, "react-select-4-input")
    
    SUBMIT_BTN = (By.ID, "submit")
    MODAL_TITLE = (By.ID, "example-modal-sizes-title-lg")
    CLOSE_MODAL_BTN = (By.ID, "closeLargeModal")

    def __init__(self, driver):
        super().__init__(driver)
        self.home_page = HomePage(self.driver)
        ## Cria uma instancia do Faker para gerar dados Brasileiros
        self.faker = Faker('pt_BR')

    def navigate(self):
        """Navega para a página Practice Form a partir da home."""
        self.home_page.load()
        self.home_page.click_card(self.home_page.CARD_FORMS)
        self.click_left_menu_item("Practice Form")

    def fill_form_with_random_data(self):
        self.type_text(self.FIRST_NAME_INPUT, self.faker.first_name())
        self.type_text(self.LAST_NAME_INPUT, self.faker.last_name())
        self.type_text(self.EMAIL_INPUT, self.faker.email())
        self.click(self.GENDER_MALE_RADIO)
        self.type_text(self.MOBILE_INPUT, self.faker.msisdn()[:10])
        self.type_text(self.CURRENT_ADDRESS_INPUT, self.faker.address())
        self.scroll_to_element(self.STATE_DROPDOWN)
        state_input_element = self.find_element(self.STATE_INPUT)
        state_input_element.send_keys("NCR")
        state_input_element.send_keys(Keys.ENTER)
        city_input_element = self.find_element(self.CITY_INPUT)
        city_input_element.send_keys("Delhi")
        city_input_element.send_keys(Keys.ENTER)

    def upload_file(self, file_path):
        self.find_element(self.UPLOAD_PICTURE_BTN).send_keys(file_path)

    def submit_form(self):
        self.scroll_to_element(self.SUBMIT_BTN)
        self.click(self.SUBMIT_BTN)

    def is_modal_visible(self):
        return self.is_element_visible(self.MODAL_TITLE)
    
    def get_modal_title(self):
        return self.get_text(self.MODAL_TITLE)

    def close_modal(self):
        self.click(self.CLOSE_MODAL_BTN)