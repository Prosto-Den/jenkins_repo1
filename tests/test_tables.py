from framework.settings.configManipulator import ConfigManipulator
from framework.driver.driver import Driver
from pages.mainPage import MainPage
from pages.elementsPage import ElementsPage
from test_data.dataManipulators import UserDataGenerator
from test_data.models import UserDataModel
from utils.tableParser import TableParser
import pytest


class TestTables:
    @pytest.mark.parametrize('user', UserDataGenerator.get_user())
    def test(self, browser, user: UserDataModel):
        Driver.instance.get(ConfigManipulator.data().URL)

        main_page = MainPage()

        assert main_page.is_displayed()

        main_page.go_to_elements_page()

        elements_page = ElementsPage()

        assert elements_page.is_displayed()

        elements_page.click_on_web_tables_btn()
        elements_page.click_on_add_button()

        assert elements_page.is_registration_form_displayed()

        table_before: tuple = TableParser.get_table_data()

        elements_page.enter_user_data(*user.as_tuple())
        elements_page.confirm_enter()

        table_after = TableParser.get_table_data()
        last_user = table_after[-1]

        assert len(table_after) > len(table_before), 'Не удалось добавить пользователя'
        assert user.as_tuple() == (last_user.first_name, last_user.last_name, last_user.email,
                                                       int(last_user.age), int(last_user.salary), last_user.department), \
            'Добавленный пользователь не соответствует пользователю из тестовых данных'

        elements_page.delete_row(len(table_after))

        table_after = TableParser.get_table_data()

        assert table_after == table_before, 'Не удалось удалить пользователя'
