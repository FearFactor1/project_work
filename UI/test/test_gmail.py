from UI.page_objects import AccountLogin, GmailPage
import pytest
import allure


class TestClassGmail:

    # 1 тест
    @allure.feature('open gmail page')
    @allure.story('Проверяем успешный логин')
    def test_open_gmail_page(self, browser, url):
        with allure.step("Открываем почту"):
            browser.get(url)
        with allure.step("Делаем логин"):
            AccountLogin(browser) \
                .input_email() \
                .button_next() \
                .input_password() \
                .button_next()
        with allure.step("Проверяем, что находимся на главной странице"):
            GmailPage(browser).find_selector_in_gpage()
            assert browser.current_url == 'https://mail.google.com/mail/u/0/#inbox'

    # 2 тест
    @allure.feature('send mail')
    @allure.story('Проверяем отправку сообщений')
    @pytest.mark.parametrize("email", ["productx905@gmail.com", "zelezodoroznik@yandex.ru"])
    @pytest.mark.parametrize("subject", ["hello", "hi"])
    def test_send_mail(self, browser, url, email, subject):
        with allure.step("Заходим в gmail"):
            browser.get(url)
        with allure.step("Делаем логин"):
            AccountLogin(browser) \
                .input_email() \
                .button_next() \
                .input_password() \
                .button_next()
        with allure.step("Заполняем письмо и отправляем"):
            GmailPage(browser).find_selector_in_gpage() \
                .button_send() \
                .find_box() \
                .input_to_and_subject_box(email, subject) \
                .button_send_in_box() \
                .send_menu_click()
        with allure.step("Проверяем, что появилось окно с текстом: письмо отправлено"):
            assert GmailPage(browser).into_send()

    # 3 тест
    @allure.feature('draft')
    @allure.story('Проверяем черновик')
    @pytest.mark.parametrize("subject", ["Всем ппривет!!", "hello", "(без темы)"])
    def test_search_draft(self, browser, url, subject):
        with allure.step("Заходим в gmail"):
            browser.get(url)
        with allure.step("Делаем логин"):
            AccountLogin(browser) \
                .input_email() \
                .button_next() \
                .input_password() \
                .button_next()
        with allure.step("Переходим в черновики"):
            GmailPage(browser).click_draft()
        with allure.step("Проверяем, что есть 3 черновика"):
            assert subject in GmailPage(browser).return_drafts()

    # 4 тест
    @allure.feature('posted')
    @allure.story('Проверяем отправленные')
    def test_search_posted(self, browser, url):
        with allure.step("Заходим в gmail"):
            browser.get(url)
        with allure.step("Делаем логин"):
            AccountLogin(browser) \
                .input_email() \
                .button_next() \
                .input_password() \
                .button_next()
        with allure.step("Переходим в тправленные"):
            GmailPage(browser).click_posted()
        with allure.step("Проверяем, что есть письмо в отправленных"):
            assert "hi" in GmailPage(browser).return_posts()

    # 5 тест
    @allure.feature('marked')
    @allure.story('Проверяем текст в меню помеченные когда ничего нет')
    def test_search_marked(self, browser, url):
        with allure.step("Заходим в gmail"):
            browser.get(url)
        with allure.step("Делаем логин"):
            AccountLogin(browser) \
                .input_email() \
                .button_next() \
                .input_password() \
                .button_next()
        with allure.step("Переходим в помеченные"):
            GmailPage(browser).click_marked()
        with allure.step("Проверяем текст когда нет помеченных писем"):
            assert "Помеченных писем нет. " \
                   "Нажмите на звездочку рядом с сообщением или цепочкой, " \
                   "чтобы пометить их и в дальнейшем " \
                   "быстро найти при необходимости." in GmailPage(browser).return_marked_text()




