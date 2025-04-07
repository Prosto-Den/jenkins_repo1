from framework.driver.driver import Driver
from framework.settings.configManipulator import ConfigManipulator
from framework.logger.logger import Logger
from test_data.dataManipulators import ProgressBarDataManipulator
from pages.mainPage import MainPage
from pages.widgetsPage import WidgetsPage
import random


class TestSlider:
    def test(self, browser):
        Logger.instance.info('Запущен тест %s ', __file__)

        Driver.instance.get(ConfigManipulator.data().URL)

        main_page = MainPage()

        assert main_page.is_displayed(), 'Не удалось загрузить страницу'

        main_page.go_to_widgets_page()

        widgets_page = WidgetsPage()

        assert widgets_page.is_displayed(), 'Не удалось загрузить страницу'

        widgets_page.click_on_slider_btn()

        assert widgets_page.is_slider_visible(), 'Не удалось загрузить страницу'

        value = random.randint(0, 100)
        Logger.instance.debug("Случайно сгенерированное значение: %d", value)

        widgets_page.set_slider_to_value(value)

        assert abs(value - widgets_page.get_slider_value()) <= 1, 'Значения не совпали'

        widgets_page.click_on_progress_bar_btn()

        assert widgets_page.is_progress_bar_visible(), 'Не удалось загрузить страницу'

        widgets_page.click_on_start_btn()

        age = ProgressBarDataManipulator.data().age

        widgets_page.click_on_stop_btn(age)

        assert abs(age - widgets_page.get_progress_bar_value()) <= 2, 'Значения не совпали'
