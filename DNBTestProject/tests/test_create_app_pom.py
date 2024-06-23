import time

import pytest

from pages.login_page import LoginPage
from pages.app_page import AppPage


class TestCreateAppPOM:
    @pytest.mark.createApp
    def test_create_app(self, driver):
        # Creating instance of page object class to call and use the function
        login_page = LoginPage(driver)
        app_page = AppPage(driver)

        # Log-In to the portal
        login_page.open()
        login_page.execute_login("nimje.trupti5@gmail.com", "Qwer@1234")
        time.sleep(2)
        print(f"Logged in successfully")
        assert login_page.is_create_app_btn_displayed, "Create app button should be visible if logged-in successfully"
        time.sleep(2)

        # Create app
        app_name = "Test app"
        app_desc = "Automating happy flow to create an app"
        app_page.create_app()
        app_page.fill_in_app_details(app_name, app_desc)
        time.sleep(2)
        print(f"Navigating to create app page")

        # Attach API
        app_page.attach_api()
        time.sleep(2)
        print(f"Attached API and App created successfully")

        # Verify app details
        res_app_name, res_app_des = app_page.verify_app_details()
        assert app_name == res_app_name, "App Name does not match"
        assert app_desc == res_app_des, "App Description does not match"
        time.sleep(2)
        print(f"App details verified successfully")

        # Delete App
        app_page.delete_app()
        print(f"App deleted successfully")
        time.sleep(2)
