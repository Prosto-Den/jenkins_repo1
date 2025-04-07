from framework.driver.driver import Driver
from selenium.webdriver.common.alert import Alert


class Alerts:
    __instance: Alert | None = None

    @classmethod
    def is_alert_displayed(cls) -> bool:
        return cls.__instance is not None

    @classmethod
    def get_alert(cls) -> None:
        cls.__instance = Driver.waiter.until(Driver.EC.alert_is_present())

    @classmethod
    def __clear(cls) -> None:
        cls.__instance = None

    @classmethod
    def click_on_alert(cls) -> None:
        cls.__instance.accept()
        cls.__clear()

    @classmethod
    def click_on_confirmation_alert(cls, is_accepted: bool) -> None:
        if is_accepted:
            cls.__instance.accept()
        else:
            cls.__instance.dismiss()

        cls.__clear()

    @classmethod
    def send_keys_to_alert(cls, keys: str) -> None:
        cls.__instance.send_keys(keys)
        cls.click_on_alert()
        cls.__clear()

