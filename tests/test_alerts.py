from pages.mainPage import MainPage
from pages.alertsPage import AlertsPage
from framework.settings.configManipulator import ConfigManipulator
from framework.utils.alerts import Alerts
from framework.driver.driver import Driver
from test_data.dataManipulators import AlertDataManipulator
from framework.logger.logger import Logger


class TestAlerts:
    def test(self, browser):
        Logger.instance.info('Запущен тест %s', __file__)

        Driver.instance.get(ConfigManipulator.data().URL)

        main_page = MainPage()
        assert main_page.is_displayed(), 'Не удалось загрузить страницу'

        main_page.go_to_alerts_page()
        alert_page = AlertsPage()
        assert alert_page.is_displayed(), 'Не удалось загрузить страницу'

        alert_page.click_alerts_btn_on_form()

        alert_page.summon_alert()
        Alerts.get_alert()
        assert Alerts.is_alert_displayed(), 'Alert не был обнаружен'
        Alerts.click_on_alert()

        alert_page.summon_timer_alert()
        Alerts.get_alert()
        assert Alerts.is_alert_displayed(), 'Alert не был обнаружен'
        Alerts.click_on_alert()

        alert_page.summon_confirm_alert()
        Alerts.get_alert()
        assert Alerts.is_alert_displayed(), 'Alert не был обнаружен'

        is_accepted: bool = AlertDataManipulator.data().is_accept
        Alerts.click_on_confirmation_alert(is_accepted)

        result: str = alert_page.get_confirm_alert_result()

        if is_accepted:
            assert result == 'ok', 'Ожидаемый результат не совпал с действительным'
        else:
            assert result == 'cancel', 'Ожидаемый результат не совпал с действительным'

        alert_page.summon_prompt_alert()
        Alerts.get_alert()
        assert Alerts.is_alert_displayed(), 'Alert не был обнаружен'

        message: str = AlertDataManipulator.data().message

        Alerts.send_keys_to_alert(message)
        result = alert_page.get_keys_alert_result()
        assert message == result, 'Ожидаемый результат не совпал с действительным'
