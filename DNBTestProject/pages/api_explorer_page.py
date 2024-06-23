import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class APIExplorer(BasePage):
    _url = 'https://developer.dnb.no/explorer/apis'
    __browser_api_option = (By.XPATH,
                            "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/header[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[2]")
    __shortcut_api_explore_option = (By.CSS_SELECTOR,
                                     "div.css-13jag4h div.eufemia-theme.eufemia-theme__prop-mapping--theme-null div.dnb-space.dnb-skeleton__root div.IF72VMPROs8g8WKBAMqN section.dnb-space.dnb-section.dnb-section--emerald-green.dnb-section--spacing-xx-large div.rBQZXOYvGtTZYZ4Qc4k8 div.dnb-div:nth-child(2) ul.IxPP82Sh8SGEftSv6sVw li:nth-child(1) > a.dnb-anchor--no-underline.dnb-anchor")
    __checkout_all_api_option = (By.XPATH, "//span[contains(text(),'Check out all our APIs')]")
    __hamburg_menu = (By.CSS_SELECTOR,
                      "div.css-13jag4h div.eufemia-theme.eufemia-theme__prop-mapping--theme-null div.dnb-space.dnb-skeleton__root div.IF72VMPROs8g8WKBAMqN header.v5hvZVw4lPq3AsXVF_pI:nth-child(1) div.Zlli1Q5MOk4KbrvRPTUI button.dnb-button.dnb-button--tertiary.dnb-button--has-text.dnb-button--icon-position-top.dnb-button--has-icon.dnb-button--icon-size-24.dnb-button--size-large:nth-child(1) span.dnb-icon.dnb-icon--medium.dnb-button__icon.dnb-icon--inherit-color > svg:nth-child(1)")
    __hamburg_menu_api_explore_option = (By.CSS_SELECTOR,
                                         "div.dnb-modal-root__inner div.dnb-modal__content.dnb-modal__content--fullscreen.eufemia-theme.eufemia-theme__prop-mapping--theme-null.dnb-dialog__root div.dnb-dialog.dnb-dialog--fullscreen.dnb-core-style.dnb-dialog--information.dnb-dialog--spacing.dnb-dialog__align--left.dnb-dialog--no-animation div.dnb-scroll-view div.dnb-dialog__inner.dnb-no-focus div.dnb-dialog__content:nth-child(3) div.dnb-space.dnb-space__top--large div.dnb-space.OA0DGqT5wdGkJHoBI4nQ.ipVn38QPYhgW9_FXiqOq div.NFKg9PwxhixQ0qTYEpsQ.dnb-space__top--medium.dnb-div div.dnb-space__top--large.dnb-div:nth-child(1) ul.dnb-ul.dnb-unstyled-list li.dnb-space__top--small.dnb-li:nth-child(2) > a.dnb-anchor.dnb-anchor--no-underline")
    __account_information_service = (By.XPATH, "//a[contains(text(),'Account Information Service')]")
    __account_pre_validation = (By.XPATH, "//a[contains(text(),'Account Pre-validation')]")
    __currencies = (By.XPATH, "//a[contains(text(),'Currencies')]")
    __payment_initiation_service = (By.XPATH, "//a[contains(text(),'Payment Initiation Service')]")
    __psd2_fallback = (By.XPATH, "//a[contains(text(),'PSD2 Fallback')]")
    __corporate_api_category_btn = (By.XPATH, "//span[contains(text(),'Corporate APIs')]")
    __regulatory_api_category_btn = (By.XPATH, "//span[contains(text(),'Regulatory APIs')]")
    __dnb_logo = (By.CSS_SELECTOR,
                  "div.css-13jag4h div.eufemia-theme.eufemia-theme__prop-mapping--theme-null div.dark-mode div.xQkiCnVRYFdH07L8ddVO.WsErVXfmmgMQ6F5ycLAQ section.dnb-space.dnb-section.dnb-section--mint-green-25:nth-child(1) div.Zlli1Q5MOk4KbrvRPTUI a.dnb-anchor--no-style:nth-child(2) span.dnb-logo.dnb-logo--inherit-size > svg:nth-child(1)")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._url

    def nav_browse_api_explorer(self):
        super()._click(self.__browser_api_option)

    def nav_shortcut_api_explorer(self):
        super()._click(self.__shortcut_api_explore_option)

    def nav_checkout_api_explorer(self):
        super()._click(self.__checkout_all_api_option)

    def nav_hamburg_menu_api_explore(self):
        super()._click(self.__hamburg_menu)
        time.sleep(2)
        super()._click(self.__hamburg_menu_api_explore_option)

    def corp_api_category(self):
        super()._click(self.__corporate_api_category_btn)
        apv_api = super()._get_text(self.__account_pre_validation)
        curr_api = super()._get_text(self.__currencies)
        return apv_api, curr_api

    def reg_api_category(self):
        super()._click(self.__regulatory_api_category_btn)
        ais_api = super()._get_text(self.__account_information_service)
        pis_api = super()._get_text(self.__payment_initiation_service)
        psd_api = super()._get_text(self.__psd2_fallback)
        return ais_api, pis_api, psd_api

    def navigate_to_main_page(self):
        super()._click(self.__dnb_logo)

    def list_all_apis(self):
        ais_api = super()._get_text(self.__account_information_service)
        apv_api = super()._get_text(self.__account_pre_validation)
        curr_api = super()._get_text(self.__currencies)
        pis_api = super()._get_text(self.__payment_initiation_service)
        psd_api = super()._get_text(self.__psd2_fallback)
        return ais_api, apv_api, curr_api, pis_api, psd_api
