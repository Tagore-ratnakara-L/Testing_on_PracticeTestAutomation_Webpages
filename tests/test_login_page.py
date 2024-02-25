# import time

import pytest

from POM_excersise.logged_in_sucessful import LoggedInSuccessfullyPage
# from selenium.webdriver.common.by import By

from POM_excersise.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        # Go to webpage
        login_page.open()

        # Type username student into Username field
        # Type password Password123 into Password field
        # Push Submit button
        login_page.execute_login("student", "Password123")

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not same as expected"
        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        assert logged_in_page.header == "Logged In Successfully", "Header is not expected"
        # Verify button Log out is displayed on the new page
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"