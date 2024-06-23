import time

import pytest

from pages.api_explorer_page import APIExplorer
from pages.login_page import LoginPage


def verify_all_apis(api_explorer_page):
    ais_api, apv_api, curr_api, pis_api, psd_api = api_explorer_page.list_all_apis()
    assert ais_api == "Account Information Service", "Listed AIS API name is not as expected"
    assert apv_api == "Account Pre-validation", "Listed APV API name is not as expected"
    assert curr_api == "Currencies", "Listed Curr API name is not as expected"
    assert pis_api == "Payment Initiation Service", "Listed PIS API name is not as expected"
    assert psd_api == "PSD2 Fallback", "Listed PSD2 API name is not as expected"
    print(f"List of All APIs:\n1.{ais_api}\n2.{apv_api}\n3.{curr_api}\n4.{pis_api}\n5.{psd_api}")


def verify_corp_api_category(api_explorer_page):
    apv_api, curr_api = api_explorer_page.corp_api_category()
    assert apv_api == "Account Pre-validation", "Listed APV API name is not as expected"
    assert curr_api == "Currencies", "Listed Curr API name is not as expected"
    print(f"List of APIs under Corporate API category is:\n1.{apv_api}\n2.{curr_api}")


def verify_reg_api_category(api_explorer_page):
    ais_api, pis_api, psd_api = api_explorer_page.reg_api_category()
    assert ais_api == "Account Information Service", "Listed AIS API name is not as expected"
    assert pis_api == "Payment Initiation Service", "Listed PIS API name is not as expected"
    assert psd_api == "PSD2 Fallback", "Listed PSD2 API name is not as expected"
    print(f"List of APIs under Regulatory API category is:\n1.{ais_api}\n2.{pis_api}\n3.{psd_api}")


class TestAPINavigationPOM:
    @pytest.mark.APINavigation
    def test_api_navigation(self, driver):
        # Creating instance of page object class to call and use the function
        login_page = LoginPage(driver)
        api_explorer_page = APIExplorer(driver)

        # Log-In to the portal
        login_page.open()
        login_page.execute_login("nimje.trupti5@gmail.com", "Qwer@1234")
        time.sleep(2)
        assert login_page.is_create_app_btn_displayed, "Create app button should be visible if logged-in successfully"
        time.sleep(2)

        # Verify navigation to API explorer from main page Browse API option
        api_explorer_page.nav_browse_api_explorer()
        assert api_explorer_page.expected_url == api_explorer_page.current_url, "Actual URL is not same as Expected URL"
        print(f"****Navigating to API Explorer from Browse API option****")

        # Verify list of all APIs
        verify_all_apis(api_explorer_page)

        # Verify list of APIs under different categories
        verify_corp_api_category(api_explorer_page)
        verify_reg_api_category(api_explorer_page)

        # Navigating back to Main page
        api_explorer_page.navigate_to_main_page()

        # Verify navigation to API explorer from Shortcuts option
        api_explorer_page.nav_shortcut_api_explorer()
        assert api_explorer_page.expected_url == api_explorer_page.current_url, "Actual URL is not same as Expected URL"
        print(f"****Navigating to API Explorer from Shortcut Menu option****")

        # Verify list of all APIs
        verify_all_apis(api_explorer_page)

        # Verify list of APIs under different categories
        verify_corp_api_category(api_explorer_page)
        verify_reg_api_category(api_explorer_page)

        # Navigating back to Main page
        api_explorer_page.navigate_to_main_page()

        # Verify navigation to API explorer from Checkout API option
        api_explorer_page.nav_checkout_api_explorer()
        assert api_explorer_page.expected_url == api_explorer_page.current_url, "Actual URL is not same as Expected URL"
        print(f"****Navigating to API Explorer from Checkout API option****")

        # Verify list of all APIs
        verify_all_apis(api_explorer_page)

        # Verify list of APIs under different categories
        verify_corp_api_category(api_explorer_page)
        verify_reg_api_category(api_explorer_page)

        # Navigating back to Main page
        api_explorer_page.navigate_to_main_page()
        time.sleep(5)

        # Verify navigation to API explorer from Hamburg Menu option
        api_explorer_page.nav_hamburg_menu_api_explore()
        assert api_explorer_page.expected_url == api_explorer_page.current_url, "Actual URL is not same as Expected URL"
        print(f"****Navigating to API Explorer from Hamburg Menu option****")

        # Verify list of all APIs
        verify_all_apis(api_explorer_page)

        # Verify list of APIs under different categories
        verify_corp_api_category(api_explorer_page)
        verify_reg_api_category(api_explorer_page)
