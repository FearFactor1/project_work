from .BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AccountLogin(BasePage):

    EMAIL = 'productx905@gmail.com'
    PASSWORD = 'Pipoum5xv'

    def input_email(self):
        em = self.driver.find_element_by_css_selector("input[type=email]")
        em.send_keys(self.EMAIL)
        return self

    def button_next(self):
        self.driver.find_element_by_css_selector(".VfPpkd-RLmnJb").click()
        return self

    def input_password(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type=password]"))
        ).send_keys(self.PASSWORD)
        return self