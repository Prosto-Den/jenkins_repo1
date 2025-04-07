from framework.pages.baseForm import BaseForm
from framework.elements.input import Input
from framework.driver.driver import Driver
from framework.elements.button import Button
from pages.leftPanel import LeftPanel
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class WidgetsPage(BaseForm):
    __LEFT_PANEL = LeftPanel()
    __SLIDER = Input("//input[@type='range']", 'Slider')
    __SLIDER_VALUE = Input("//input[@id='sliderValue']", 'Slider Value')
    __START_STOP_BTN = Button("//button[@id='startStopButton']", 'Start/stop progress bar Btn')
    __PROGRESS_BAR: tuple[str, str] = (By.XPATH, "//div[@id='progressBar']")
    __PROGRESS_BAR_VALUE: tuple[str, str] = (By.XPATH, "//div[@role='progressbar']")

    def __init__(self) -> None:
        super().__init__("//div[@class = 'left-pannel']", 'Widgets Page')

    def click_on_slider_btn(self) -> None:
        self.__LEFT_PANEL.click_on_slider_btn()

    def click_on_progress_bar_btn(self) -> None:
        self.__LEFT_PANEL.click_on_progress_bar_btn()

    def click_on_start_btn(self) -> None:
        self.__START_STOP_BTN.click()

    def click_on_stop_btn(self, value: int) -> None:
        Driver.waiter.until(lambda _: self.get_progress_bar_value() + 4 >= value)

        self.__START_STOP_BTN.click()

    def is_slider_visible(self) -> bool:
        return self.__SLIDER.is_displayed()

    def is_progress_bar_visible(self) -> bool:
        return Driver.waiter.until(Driver.EC.presence_of_element_located(self.__PROGRESS_BAR)).is_displayed()

    def set_slider_to_value(self, value: int) -> None:
        slider = self.__SLIDER.find_element()

        min_value = int(slider.get_dom_attribute('min'))
        max_value = int(slider.get_dom_attribute('max'))
        width = slider.size['width']
        offset_x = value * width / (max_value - min_value) + 2

        (ActionChains(Driver.instance).move_to_element(slider).move_by_offset(-width / 2, 0)
         .click_and_hold().move_by_offset(offset_x, 0).release().perform())

    def get_slider_value(self) -> int:
        slider_value = self.__SLIDER_VALUE.find_element()

        return int(slider_value.get_dom_attribute('value'))

    def get_progress_bar_value(self) -> int:
        element = Driver.instance.find_element(*self.__PROGRESS_BAR_VALUE)

        return int(element.get_dom_attribute('aria-valuenow'))

