from pages.leftPanel import LeftPanel
from framework.pages.baseForm import BaseForm
from framework.elements.button import Button
from .registration_form import RegistrationForm


class ElementsPage(BaseForm):
    __LEFT_PANEL = LeftPanel()
    __ADD_BTN = Button("//button[@id='addNewRecordButton']", "Add Button")
    __REGISTRATION_FORM = RegistrationForm()

    def __init__(self) -> None:
        super().__init__("//div[@class = 'left-pannel']", "Elements Page")

    def is_displayed(self) -> bool:
        return self.__LEFT_PANEL.is_displayed()

    def click_on_web_tables_btn(self) -> None:
        self.__LEFT_PANEL.click_on_web_tables_btn()

    def click_on_add_button(self) -> None:
        self.__ADD_BTN.click()

    def is_registration_form_displayed(self) -> bool:
        return self.__REGISTRATION_FORM.is_displayed()

    def enter_user_data(self, first_name: str,
                        last_name: str, email: str,
                        age: int, salary: int, department: str) -> None:
        self.__REGISTRATION_FORM.enter_first_name(first_name)
        self.__REGISTRATION_FORM.enter_last_name(last_name)
        self.__REGISTRATION_FORM.enter_email(email)
        self.__REGISTRATION_FORM.enter_age(age)
        self.__REGISTRATION_FORM.enter_salary(salary)
        self.__REGISTRATION_FORM.enter_department(department)

    def confirm_enter(self) -> None:
        self.__REGISTRATION_FORM.confirm_input()

    def delete_row(self, row_number: int) -> None:
        delete_btn_locator = "//span[@id='delete-record-{0}']".format(row_number)
        DELETE_BTN = Button(delete_btn_locator, "Delete Btn")
        DELETE_BTN.click()
