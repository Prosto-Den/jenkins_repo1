from framework.elements.button import Button
from framework.pages.baseForm import BaseForm


class MainPage(BaseForm):

    __ALERTS_BTN = Button("//*[contains(text(),'Alerts')]", "Alerts Btn")
    __ELEMENTS_BTN = Button("//div[contains(@class, 'top-card') and contains(.,'Elements')]",
                            'Elements Btn')
    __WIDGETS_BTN = Button("//div[contains(@class, 'top-card') and contains(.,'Widgets')]", 'Widgets Btn')

    def __init__(self) -> None:
        super().__init__('//header//img', 'Main Page')

    def go_to_alerts_page(self) -> None:
        self.__ALERTS_BTN.click()

    def go_to_elements_page(self) -> None:
        self.__ELEMENTS_BTN.click()

    def go_to_widgets_page(self) -> None:
        self.__WIDGETS_BTN.click()