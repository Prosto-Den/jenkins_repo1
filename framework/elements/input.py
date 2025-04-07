from framework.elements.baseElement import BaseElement
from framework.logger.logger import Logger


class Input(BaseElement):
    def __init__(self, locator: str, name: str) -> None:
        super().__init__(locator, name)

    def send_keys(self, value: str) -> None:
        Logger.instance.info('В поле %s введено значение "%s"', self._name, value)
        self.find_element().send_keys(value)
