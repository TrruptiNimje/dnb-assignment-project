from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://developer.dnb.no/"
    __popup = (By.XPATH, "//a[contains(text(),'OK')]")
    __signin_btn = (By.CSS_SELECTOR, ".dnb-button--tertiary:nth-child(3) > .dnb-button__text")
    __email_field = (By.XPATH, "//div[@id=\'app\']/div/div/section/div/div/div[2]/div/div/form/div/div/div/span/span/span[2]/span/input")
    __password_field = (By.XPATH, "//div[@id=\'app\']/div/div/section/div/div/div[2]/div/div/form/div[2]/div/div/div/div/div[2]/span/span/span[2]/span/input")
    __login_btn = (By.CSS_SELECTOR, "div.css-13jag4h div.eufemia-theme.eufemia-theme__prop-mapping--theme-null section.dnb-space.dnb-section.dnb-section--black-3 div.KDeuNahyFzO5usxs_2yJ.dnb-div div.dnb-space.dnb-skeleton__root div.dnb-space.OA0DGqT5wdGkJHoBI4nQ.ipVn38QPYhgW9_FXiqOq div.dnb-space.dnb-space__top--large div.dnb-space.dnb-space__top--small.ipVn38QPYhgW9_FXiqOq.U6zgOcoti5aSNKT56z8D form.dnb-form-set div.dnb-form-row__fieldset:nth-child(4) div.dnb-space.dnb-section.dnb-section--transparent.dnb-form-row.dnb-form-row--vertical.dnb-form-row--vertical-label.dnb-space__top--large div.dnb-form-row__content button.dnb-button.dnb-button--primary.dnb-button--has-text.dnb-button--icon-position-left.dnb-button--has-icon.dnb-button--icon-size-medium.dnb-button--size-large > span.dnb-button__text.dnb-skeleton--show-font")
    __create_app_locator = (By.XPATH, "//span[contains(text(),'Create app')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, email: str, password: str):
        super()._click(self.__popup)
        super()._click(self.__signin_btn)
        super()._type(self.__email_field, email)
        super()._type(self.__password_field, password)
        super()._click(self.__login_btn)

    @property
    def is_create_app_btn_displayed(self) -> bool:
        return super()._is_displayed(self.__create_app_locator)
