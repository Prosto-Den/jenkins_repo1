from framework.pages.baseForm import BaseForm
from framework.elements.button import Button
from framework.elements.label import Label
from .leftPanel import LeftPanel
from framework.driver.driver import Driver
from selenium.webdriver.common.by import By


class AlertsPage(BaseForm):
    __LEFT_PANEL = LeftPanel()

    __ALERT_BTN = Button("//button[@id='alertButton']", "Alert Btn")
    __TIMER_ALERT_BTN = Button("//button[@id='timerAlertButton']", "Timer Alert Btn")
    __CONFIRM_ALERT_BTN = Button("//button[@id='confirmButton']", "Confirm Alert Btn")
    __PROMPT_ALERT_BTN = Button("//button[@id='promtButton']", "Prompt Alert Btn")
    __NEW_TAB_BTN = Button("//button[@id='tabButton']", "New Tab Button")
    __HOME_LINK = Button("//a[@id='simpleLink']", "Home Link")

    __CONFIRM_RESULT_LABEL = Label("//span[@id = 'confirmResult']", "Confirm Result")
    __PROMPT_RESULT_LABEL = Label("//span[@id = 'promptResult']", "Prompt Result")
    __PARENT_IFRAME_LABEL = Label(    "//body[contains(.,'Parent frame')]", "Parent Frame Label")
    __CHILD_IFRAME_LABEL = Label("//p[contains(.,'Child')]", "Child Iframe Label")
    __FRAME_LABEL = Label("//h1[@id='sampleHeading']", "Frame Label")
    __CENTER_LABEL = Label("//*[@class='text-center']", "Center Label")

    __PARENT_IFRAME = BaseForm("//iframe[@id='frame1']", "Parent IFrame")
    __CHILD_IFRAME = BaseForm("//iframe", "Child IFrame")
    __FIRST_FRAME = BaseForm("//iframe[@id='frame1']", "First Frame")
    __SECOND_FRAME = BaseForm("//iframe[@id='frame2']", "Second Frame")

    def __init__(self) -> None:
        super().__init__("//div[@class = 'left-pannel']", "Alert Page")

    def __switch_to_parent_iframe(self) -> None:
        Driver.instance.switch_to.frame("frame1")

    def __switch_to_child_iframe(self) -> None:
        iframe = Driver.instance.find_element(By.TAG_NAME, "iframe")
        Driver.instance.switch_to.frame(iframe)

    def click_alerts_btn_on_form(self) -> None:
        self.__LEFT_PANEL.click_on_alerts()

    def click_nested_frames_btn_on_form(self) -> None:
        self.__LEFT_PANEL.click_on_nested_frames_btn()

    def click_frames_btn_on_form(self) -> None:
        self.__LEFT_PANEL.click_on_frames_btn()

    def click_browser_windows_btn_on_form(self) -> None:
        self.__LEFT_PANEL.click_on_browser_windows_btn()

    def click_on_home_link(self) -> None:
        self.__HOME_LINK.click()

    def summon_alert(self) -> None:
        self.__ALERT_BTN.click()

    def summon_timer_alert(self) -> None:
        self.__TIMER_ALERT_BTN.click()

    def summon_confirm_alert(self) -> None:
        self.__CONFIRM_ALERT_BTN.click()

    def summon_prompt_alert(self) -> None:
        self.__PROMPT_ALERT_BTN.click()

    def summon_new_tab(self) -> None:
        self.__NEW_TAB_BTN.click()

    def get_confirm_alert_result(self) -> str:
        return self.__CONFIRM_RESULT_LABEL.text.split(" ")[-1].lower()

    def get_keys_alert_result(self) -> str:
        return self.__PROMPT_RESULT_LABEL.text.split(" ")[-1].lower()

    def click_on_elements_group(self) -> None:
        self.__LEFT_PANEL.click_on_elements_group_btn()

    def click_on_links_btn(self) -> None:
        self.__LEFT_PANEL.click_on_links_btn()

    def exit_iframe(self) -> None:
        Driver.instance.switch_to.default_content()

    def is_iframe_displayed(self) -> bool:
        return self.__PARENT_IFRAME.is_displayed()

    def is_parent_label_displayed(self) -> bool:
        self.__switch_to_parent_iframe()

        return self.__PARENT_IFRAME_LABEL.text != ""

    def is_child_label_displayed(self) -> bool:
        self.__switch_to_child_iframe()

        return self.__CHILD_IFRAME_LABEL.text != ""

    def is_frame_displayed(self) -> bool:
        return self.__FIRST_FRAME.is_displayed()

    def is_browser_window_form_displayed(self) -> bool:
        return self.__CENTER_LABEL.is_displayed() and self.__CENTER_LABEL.text == "Browser Windows"

    def is_links_window_displayed(self) -> bool:
        return self.__CENTER_LABEL.is_displayed() and self.__CENTER_LABEL.text == "Links"

    def get_first_frame_label(self) -> str:
        Driver.instance.switch_to.frame("frame1")
        result = self.__FRAME_LABEL.find_element().text
        self.exit_iframe()

        return result

    def get_second_frame_label(self) -> str:
        Driver.instance.switch_to.frame("frame2")
        result = self.__FRAME_LABEL.find_element().text
        self.exit_iframe()

        return result
