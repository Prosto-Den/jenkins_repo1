from framework.pages.baseForm import BaseForm
from framework.elements.button import Button


class LeftPanel(BaseForm):
    __ALERTS_BTN = Button("//li[contains(., 'Alerts')]",
                          "Alerts Btn")
    __NESTED_FRAMES_BTN = Button("//li[contains(., 'Nested')]",
                                 'Nested Frames Btn')
    __FRAMES_BTN = Button("//li[. = 'Frames']", 'Frames Btn')
    __WEB_TABLES_BTN = Button("//li[.='Web Tables']", 'Web Tables Btn')
    __BROWSER_WINDOWS_BTN = Button("//li[.='Browser Windows']", 'Browser Windows Btn')
    __ELEMENTS_GROUP_BTN = Button("//div[contains(., 'Elements') and @class='element-group']",
                                  'Element Group Btn')
    __LINKS_BTN = Button("//li[.='Links']", 'Links Btn')
    __SLIDER_BTN = Button("//li[.='Slider']", "Slider Btn")
    __PROGRESS_BAR_BTN = Button("//li[.='Progress Bar']", 'Progress Bar Btn')

    def __init__(self) -> None:
        super().__init__("//div[@class = 'left-pannel']", "Left Panel")

    def click_on_alerts(self) -> None:
        self.__ALERTS_BTN.click()

    def click_on_nested_frames_btn(self) -> None:
        self.__NESTED_FRAMES_BTN.click()

    def click_on_frames_btn(self) -> None:
        self.__FRAMES_BTN.click()

    def click_on_web_tables_btn(self) -> None:
        self.__WEB_TABLES_BTN.click()

    def click_on_browser_windows_btn(self) -> None:
        self.__BROWSER_WINDOWS_BTN.click()

    def click_on_elements_group_btn(self) -> None:
        self.__ELEMENTS_GROUP_BTN.click()

    def click_on_links_btn(self) -> None:
        self.__LINKS_BTN.click()

    def click_on_slider_btn(self) -> None:
        self.__SLIDER_BTN.click()

    def click_on_progress_bar_btn(self) -> None:
        self.__PROGRESS_BAR_BTN.click()