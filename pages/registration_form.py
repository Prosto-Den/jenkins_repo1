from framework.pages.baseForm import BaseForm
from framework.elements.input import Input
from framework.elements.button import Button


class RegistrationForm(BaseForm):
    __FIRST_NAME_INPUT = Input("//input[@id='firstName']", 'Input First Name')
    __LAST_NAME_INPUT = Input("//input[@id='lastName']", 'Input Last Name')
    __EMAIL_INPUT = Input("//input[@id='userEmail']", 'Input Email')
    __AGE_INPUT = Input("//input[@id='age']", 'Input Age')
    __SALARY_INPUT = Input("//input[@id='salary']", 'Input Salary')
    __DEPARTMENT_INPUT = Input("//input[@id='department']", 'Input Department')
    __SUBMIT_BUTTON = Button("//button[@id='submit']", 'Btn Submit')

    def __init__(self) -> None:
        super().__init__("//div[@class='modal-content']", 'Registration Form')

    def enter_first_name(self, first_name: str) -> None:
        self.__FIRST_NAME_INPUT.send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.__LAST_NAME_INPUT.send_keys(last_name)

    def enter_email(self, email: str) -> None:
        self.__EMAIL_INPUT.send_keys(email)

    def enter_age(self, age: int) -> None:
        self.__AGE_INPUT.send_keys(str(age))

    def enter_salary(self, salary: int) -> None:
        self.__SALARY_INPUT.send_keys(str(salary))

    def enter_department(self, department: str) -> None:
        self.__DEPARTMENT_INPUT.send_keys(department)

    def confirm_input(self) -> None:
        self.__SUBMIT_BUTTON.click()