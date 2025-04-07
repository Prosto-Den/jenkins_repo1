from framework.settings.configManipulator import ConfigManipulator
from framework.driver.driver import Driver
from framework.logger.logger import Logger
from pages.mainPage import MainPage
from pages.alertsPage import AlertsPage
from pages.samplePage import SamplePage


class TestHandles:
    def test(self, browser):
        Logger.instance.info('Запущен тест %s ', __file__)

        Driver.instance.get(ConfigManipulator.data().URL)

        main_page = MainPage()

        assert main_page.is_displayed(), 'Не удалось загрузить страницу'

        main_page.go_to_alerts_page()

        alerts_page = AlertsPage()

        assert alerts_page.is_displayed(), 'Не удалось загрузить страницу'

        alerts_page.click_browser_windows_btn_on_form()

        assert alerts_page.is_browser_window_form_displayed(), 'Не удалось загрузить страницу'

        alerts_page.summon_new_tab()

        sample_page = SamplePage()

        assert len(Driver.instance.window_handles) == 2, 'Новая вкладка не была открыта'

        Driver.instance.switch_to.window(Driver.instance.window_handles[1])

        assert sample_page.is_displayed(), 'Не удалось загрузить страницу'
        assert '/sample' in Driver.instance.current_url, 'Открыта не та страница'

        sample_page.close()
        Driver.instance.switch_to.window(Driver.instance.window_handles[0])

        assert alerts_page.is_browser_window_form_displayed(), 'Не удалось загрузить страницу'

        alerts_page.click_on_elements_group()
        alerts_page.click_on_links_btn()

        assert alerts_page.is_links_window_displayed()

        alerts_page.click_on_home_link()

        assert len(Driver.instance.window_handles) == 2

        main_page = MainPage()
        Driver.instance.switch_to.window(Driver.instance.window_handles[1])

        assert main_page.is_displayed()
        Driver.instance.switch_to.window(Driver.instance.window_handles[0])

        assert alerts_page.is_links_window_displayed()