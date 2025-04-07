from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver as wd
from ..settings.configManipulator import ConfigManipulator
from screeninfo import get_monitors
from screeninfo.common import Monitor
from framework.singleton.singleton import Singleton


class Driver(metaclass=Singleton):
    instance: WebDriver | None = None
    waiter: WebDriverWait | None = None
    EC = EC

    @classmethod
    def init(cls):
        cls.instance = cls.__create_driver()
        cls.waiter = WebDriverWait(cls.instance, ConfigManipulator.data().delay)
        cls.EC = EC

    @classmethod
    def close(cls) -> None:
        cls.instance.quit()
        cls.instance = None
        cls.waiter = None

    @classmethod
    def __create_driver(cls) -> WebDriver:
        match ConfigManipulator.data().current_browser:
            case 'CHROME':
                options = wd.ChromeOptions()

                if ConfigManipulator.data().fullscreen:
                    options.add_argument('--start-maximized')

                if ConfigManipulator.data().incognito:
                    options.add_argument('--incognito')

                options.add_argument(f'--lang={ConfigManipulator.data().language}')
                options.page_load_strategy = ConfigManipulator.data().load_strategy

                return wd.Chrome(options=options)

            case 'FIREFOX':
                monitor: Monitor = get_monitors()[0]
                monitor_size = (monitor.width, monitor.height)

                options = wd.FirefoxOptions()

                if ConfigManipulator.data().fullscreen:
                    options.add_argument(f'--width={monitor_size[0]}')
                    options.add_argument(f'--height={monitor_size[1]}')

                if ConfigManipulator.data().incognito:
                    options.add_argument('-private-window')

                options.set_preference('intl.accept_languages', ConfigManipulator.data().language)
                options.page_load_strategy = ConfigManipulator.data().load_strategy

                return wd.Firefox(options=options)

            case _:
                raise ValueError('Данный браузер не поддерживается')
