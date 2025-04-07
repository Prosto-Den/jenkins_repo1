from framework.driver.driver import Driver
from framework.logger.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BaseElement:
    def __init__(self, locator: str, name: str) -> None:
        self._locator: tuple[str, str] = (By.XPATH, locator)
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def text(self):
        return Driver.waiter.until(Driver.EC.presence_of_element_located(self._locator)).text

    def click(self):
        Logger.instance.info('Нажатие на %s', self.name)
        self.find_element().click()

    def find_element(self) -> WebElement:
        Logger.instance.debug('Поиск элемента %s', self._name)
        return Driver.waiter.until(Driver.EC.visibility_of_element_located(self._locator))

    def is_displayed(self) -> bool:
        return self.find_element().is_displayed()
