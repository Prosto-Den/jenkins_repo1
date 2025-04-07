from framework.settings.configManipulator import ConfigManipulator
from framework.driver.driver import Driver
from framework.logger.logger import Logger
from pages.mainPage import MainPage
from pages.alertsPage import AlertsPage


class TestIFrames:
    def test(self, browser):
        Logger.instance.info('Запущен тест %s ', __file__)

        Driver.instance.get(ConfigManipulator.data().URL)

        main_page = MainPage()

        if main_page.is_displayed():
            main_page.go_to_alerts_page()

        alert_page = AlertsPage()

        if alert_page.is_displayed():
            alert_page.click_nested_frames_btn_on_form()

        if alert_page.is_iframe_displayed():
            assert alert_page.is_parent_label_displayed(), 'Надпись родительского IFrame на найдена'
            assert alert_page.is_child_label_displayed(), 'Надпись дочернего IFrame не найдена'

        alert_page.exit_iframe()

        alert_page.click_frames_btn_on_form()

        if alert_page.is_frame_displayed():
            assert alert_page.get_first_frame_label() == alert_page.get_second_frame_label(), \
                'Надписи не совпадают'
