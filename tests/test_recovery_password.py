import allure
import urls

from conftest import driver
from pages.login_page import LoginPage
from pages.recovery_password_page import RecoveryPasswordPage


class TestRecoveryPassword:
    @allure.title('Проверка восстановления пароля')
    @allure.description('Клик по кнопке "Восстановлние пароля" ведет на страницу восстановления пароля')
    def test_click_recovery_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page_login()
        login_page.click_recovery_password()
        assert login_page.get_current_url() == urls.UrlStBurgers.URL + urls.UrlStBurgers.URL_FORGOT_PASSWORD

    @allure.description('Ввод почты и клик по кнопке Восстановить')
    def test_put_email_and_click_button_recovery(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.open_page_recovery_password()
        recovery_password_page.input_email()
        recovery_password_page.click_button_recovery()
        assert recovery_password_page.get_current_url() == urls.UrlStBurgers.URL + urls.UrlStBurgers.URL_RESET_PASSWORD

    @allure.description('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_show_hide_password_field(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.open_page_recovery_password()
        recovery_password_page.input_email()
        recovery_password_page.click_button_recovery()
        recovery_password_page.input_password()
        recovery_password_page.click_sign_eye()
        assert recovery_password_page.check_password_field



