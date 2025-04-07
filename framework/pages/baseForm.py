from framework.driver.driver import Driver
from framework.logger.logger import Logger
from selenium.webdriver.common.by import By


class BaseForm:
    def __init__(self, locator: str, name: str) -> None:
        self._locator: tuple[str, str] = (By.XPATH, locator)
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def is_displayed(self) -> bool:
        Logger.instance.info('Открытие страницы %s', self._name)
        return Driver.waiter.until(Driver.EC.visibility_of_element_located(self._locator)).is_displayed()

    def close(self) -> None:
        Driver.instance.close()