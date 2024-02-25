from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
from POM_excersise.basePage import  BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submission_button = (By.XPATH, "//button[@class='btn']")
    __error_message = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submission_button)

    def get_error_message(self) -> str:
        return super()._get_text(self.__error_message, 5)

        # """Add wait before process"""
        # wait = WebDriverWait(self._driver, 10)

        # """type username into username field """
        # # username_locator = self._driver.find_element(self.__username_field)
        # # username_locator.send_keys(username)
        # wait.until(ec.visibility_of_element_located(self.__username_field))
        # self._driver.find_element(self.__username_field).send_keys(username)
        #
        # """type password into password field """
        # wait.until(ec.visibility_of_element_located(self.__password_field))
        # self._driver.find_element(self.__username_field).send_keys(password)
        #
        # """Click on submit button"""
        # wait.until(ec.visibility_of_element_located(self.__submission_button))
        # self._driver.find_element(self.__submission_button).click()
