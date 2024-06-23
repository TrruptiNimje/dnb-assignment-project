from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class AppPage(BasePage):
    __create_app_locator = (By.XPATH, "//span[contains(text(),'Create app')]")
    __app_name_field = (By.XPATH, "//body[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/span[1]/span[1]/span[2]/span[1]/input[1]")
    __app_desc_field = (By.XPATH, "//body[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/span[1]/span[1]/span[2]/span[1]/textarea[1]")
    __app_nxt_btn = (By.CSS_SELECTOR, "div.css-13jag4h div.eufemia-theme.eufemia-theme__prop-mapping--theme-null section.dnb-space.dnb-section.dnb-section--black-3 div.KDeuNahyFzO5usxs_2yJ.dnb-div div.dnb-space.dnb-skeleton__root div.dnb-space.OA0DGqT5wdGkJHoBI4nQ.ipVn38QPYhgW9_FXiqOq.RwKMt8VkJp3lCf9ZXEHg div.dnb-space.dnb-space__top--large div.dnb-space.dnb-flex-container.dnb-flex-container--direction-horizontal.dnb-flex-container--justify-flex-start.dnb-flex-container--align-flex-start.dnb-flex-container--spacing-small.dnb-flex-container--divider-space div.dnb-space.dnb-space__right--small.dnb-space__left--zero.dnb-flex-item.dnb-flex-item--grow:nth-child(2) div.dnb-space.dnb-space--stretch form.dnb-form-set div.dnb-form-row__fieldset:nth-child(5) div.dnb-space.dnb-section.dnb-section--transparent.dnb-form-row.dnb-space__top--medium div.dnb-form-row__content button.dnb-button.dnb-button--primary.dnb-button--has-text.dnb-space__right--medium.dnb-button--icon-position-right.dnb-button--has-icon.dnb-button--size-large > span.dnb-button__text.dnb-skeleton--show-font")
    __api_checkbox = (By.XPATH, "//body[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/span[1]/span[2]/input[1]")
    __api_nxt_btn = (By.CSS_SELECTOR, "div.css-13jag4h div.eufemia-theme.eufemia-theme__prop-mapping--theme-null section.dnb-space.dnb-section.dnb-section--black-3 div.KDeuNahyFzO5usxs_2yJ.dnb-div div.dnb-space.dnb-skeleton__root div.dnb-space.OA0DGqT5wdGkJHoBI4nQ.ipVn38QPYhgW9_FXiqOq.RwKMt8VkJp3lCf9ZXEHg div.dnb-space.dnb-space__top--large div.dnb-space.dnb-flex-container.dnb-flex-container--direction-horizontal.dnb-flex-container--justify-flex-start.dnb-flex-container--align-flex-start.dnb-flex-container--spacing-small.dnb-flex-container--divider-space div.dnb-space.dnb-space__right--small.dnb-space__left--zero.dnb-flex-item.dnb-flex-item--grow:nth-child(2) div.dnb-space.dnb-space--stretch form.dnb-form-set div.dnb-form-row__fieldset:nth-child(2) div.dnb-space.dnb-section.dnb-section--transparent.dnb-form-row.dnb-space__top--medium div.dnb-form-row__content > button.dnb-button.dnb-button--primary.dnb-button--has-text.dnb-space__right--medium.dnb-button--icon-position-right.dnb-button--has-icon.dnb-button--size-large:nth-child(2)")
    __api_scope_nxt_btn = (By.CSS_SELECTOR, "div.css-13jag4h div.eufemia-theme.eufemia-theme__prop-mapping--theme-null section.dnb-space.dnb-section.dnb-section--black-3 div.KDeuNahyFzO5usxs_2yJ.dnb-div div.dnb-space.dnb-skeleton__root div.dnb-space.OA0DGqT5wdGkJHoBI4nQ.ipVn38QPYhgW9_FXiqOq.RwKMt8VkJp3lCf9ZXEHg div.dnb-space.dnb-space__top--large div.dnb-space.dnb-flex-container.dnb-flex-container--direction-horizontal.dnb-flex-container--justify-flex-start.dnb-flex-container--align-flex-start.dnb-flex-container--spacing-small.dnb-flex-container--divider-space div.dnb-space.dnb-space__right--small.dnb-space__left--zero.dnb-flex-item.dnb-flex-item--grow:nth-child(2) div.dnb-space.dnb-space--stretch form.dnb-form-set div.dnb-form-row__fieldset:nth-child(2) div.dnb-space.dnb-section.dnb-section--transparent.dnb-form-row.dnb-space__top--medium div.dnb-form-row__content button.dnb-button.dnb-button--primary.dnb-button--has-text.dnb-space__right--medium.dnb-button--icon-position-right.dnb-button--has-icon.dnb-button--size-large:nth-child(2) > span.dnb-button__text.dnb-skeleton--show-font")
    __create_app_btn = (By.XPATH, "//body[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/button[2]/span[2]")
    __app_created_msg = (By.XPATH, "//body[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h2[2]")
    __goto_app_btn = (By.XPATH, "//span[contains(text(),'Go to application')]")
    __given_app_name = (By.XPATH, "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/section[2]/div[1]/div[3]/p[2]")
    __given_app_desc = (By.XPATH, "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/section[2]/div[1]/div[4]/p[2]")
    __delete_app_btn = (By.XPATH, "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/section[3]/button[1]/span[2]")
    __confirm_delete_btn = (By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[3]/button[2]/span[2]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 20)

    def create_app(self):
        super()._click(self.__create_app_locator)

    def fill_in_app_details(self, app_name: str, app_desc: str):
        super()._type(self.__app_name_field, app_name)
        super()._type(self.__app_desc_field, app_desc)
        super()._click(self.__app_nxt_btn)

    def attach_api(self):
        super()._click_chk_box(self.__api_checkbox)
        super()._click(self.__api_nxt_btn)
        super()._click(self.__api_scope_nxt_btn)
        super()._click(self.__create_app_btn)
        super()._get_text(self.__app_created_msg)
        super()._click(self.__goto_app_btn)

    def verify_app_details(self):
        verification_app_name = super()._get_text(self.__given_app_name)
        verification_app_desc = super()._get_text(self.__given_app_desc)
        return verification_app_name, verification_app_desc

    def delete_app(self):
        super()._click(self.__delete_app_btn)
        super()._click(self.__confirm_delete_btn)
