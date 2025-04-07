from framework.driver.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from test_data.models import UserDataModel
from dataclasses import dataclass


@dataclass
class RowModel:
    first_name: str
    last_name: str
    age: str
    email: str
    salary: str
    department: str


class TableParser:
    __HEADER_LOCATOR: tuple[str, str] = (By.XPATH, "//div[contains(@class, 'rt-thead')]/child::*")
    __CELL_LOCATOR: tuple[str, str] = (By.XPATH, "//div[@class='rt-td']")
    __data: list[UserDataModel] = []

    @classmethod
    def get_header(cls) -> tuple[str, ...]:
        header: WebElement = Driver.waiter.until(Driver.EC.presence_of_element_located(cls.__HEADER_LOCATOR))

        cols: list[WebElement] = header.find_elements(By.XPATH, "//div[contains(@class, 'header-content')]")

        result = []
        for item in cols:
            result.append(item.text)

        return tuple(result)

    @classmethod
    def get_table_data(cls):
        cells: list[WebElement] = Driver.instance.find_elements(*cls.__CELL_LOCATOR)
        header: tuple[str, ...] = cls.get_header()

        result = []
        for index in range(0, len(cells), len(header)):
            row = cells[index:index + len(header) - 1]

            if row[0].text == ' ':
                break

            sub_list = []
            for item in row:
                sub_list.append(item.text)

            result.append(RowModel(*sub_list))

        return tuple(result)