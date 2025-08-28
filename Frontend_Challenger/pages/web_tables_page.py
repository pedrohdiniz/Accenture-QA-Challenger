from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.home_page import HomePage
from faker import Faker
from selenium.common.exceptions import TimeoutException

class WebTablesPage(BasePage):
    # Locators
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    SUBMIT_BUTTON = (By.ID, "submit")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    AGE_INPUT = (By.ID, "age")
    SALARY_INPUT = (By.ID, "salary")
    DEPARTMENT_INPUT = (By.ID, "department")
    TABLE_ROW = (By.CSS_SELECTOR, ".rt-tr-group")
    ROW_WITH_TEXT = "//div[@class='rt-td' and text()='{}']/parent::div"
    ALL_DELETE_ICONS = (By.XPATH, "//span[@title='Delete']")

    def __init__(self, driver):
        super().__init__(driver)
        self.home_page = HomePage(self.driver)
        self.faker = Faker('pt_BR')

    def navigate(self):
        self.home_page.load()
        self.home_page.click_card(self.home_page.CARD_ELEMENTS)
        self.click_left_menu_item("Web Tables")
    
    def fill_registration_form(self, data=None):
        if not data:
            data = {
                "first_name": self.faker.first_name(),
                "last_name": self.faker.last_name(),
                "email": self.faker.email(),
                "age": str(self.faker.random_int(min=18, max=70)),
                "salary": str(self.faker.random_int(min=1000, max=10000)),
                "department": self.faker.job().replace("'", "")
            }
        
        self.type_text(self.FIRST_NAME_INPUT, data["first_name"])
        self.type_text(self.LAST_NAME_INPUT, data["last_name"])
        self.type_text(self.EMAIL_INPUT, data["email"])
        self.type_text(self.AGE_INPUT, data["age"])
        self.type_text(self.SALARY_INPUT, data["salary"])
        self.type_text(self.DEPARTMENT_INPUT, data["department"])
        return data

    def add_new_record(self):
        self.click(self.ADD_BUTTON)
        user_data = self.fill_registration_form()
        self.click(self.SUBMIT_BUTTON)
        return user_data

    def edit_record(self, email_to_find):
        edit_locator = (By.XPATH, self.ROW_WITH_TEXT.format(email_to_find) + "//span[@title='Edit']")
        self.scroll_to_element(edit_locator)
        self.click(edit_locator)
        new_user_data = self.fill_registration_form()
        self.click(self.SUBMIT_BUTTON)
        return new_user_data
        
    def delete_record(self, email_to_find):
        delete_locator = (By.XPATH, self.ROW_WITH_TEXT.format(email_to_find) + "//span[@title='Delete']")
        self.scroll_to_element(delete_locator)
        self.click(delete_locator)
    
    def is_record_present(self, email):
        locator = (By.XPATH, self.ROW_WITH_TEXT.format(email))
        return self.is_element_visible(locator, timeout=2)

    def get_row_count(self):
        rows = self.find_elements(self.TABLE_ROW)
        return len([row for row in rows if len(row.text.strip()) > 0])
    
    def add_multiple_records(self, count):
        for _ in range(count):
            self.add_new_record()

    def delete_all_added_records(self, initial_count):
        """
        Deleta todos os registros adicionados, um por um.
        """
        while self.get_row_count() > initial_count:
            delete_icons = self.find_elements(self.ALL_DELETE_ICONS)           
            delete_icons[initial_count].click()