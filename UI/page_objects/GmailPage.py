from .BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class GmailPage(BasePage):

    LETTER_TEXT = "Всем привет!!"

    def find_selector_in_gpage(self):
        WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "div[data-tooltip=Входящие]"))
        )
        return self

    def button_send(self):
        self.driver.find_element_by_css_selector(".T-I.T-I-KE.L3").click()
        return self

    def find_box(self):
        WebDriverWait(self.driver, 7).until(
            EC.text_to_be_present_in_element(
                (
                    By.CSS_SELECTOR, ".aYF"),
                "Новое сообщение")
        )
        return self

    def input_to_and_subject_box(self, email, subject):
        it = self.driver.find_element_by_css_selector(".vO")
        it.send_keys(email)
        sb = self.driver.find_element_by_css_selector(".aoT")
        sb.send_keys(subject)
        letter_text = self.driver.find_element_by_css_selector(".LW-avf.tS-tW")
        letter_text.send_keys(self.LETTER_TEXT)
        return self

    def button_send_in_box(self):
        self.driver.find_element_by_css_selector(".v7.T-I-atl.L3").click()
        return self

    def send_menu_click(self):
        WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located((
                By.LINK_TEXT, "Отправленные"))
        )
        self.driver.find_element_by_link_text("Отправленные").click()
        return self

    def into_send(self):
        WebDriverWait(self.driver, 7).until(
            EC.text_to_be_present_in_element(
                (
                    By.CSS_SELECTOR, ".bAq"),
                "Письмо отправлено.")
        )
        return self