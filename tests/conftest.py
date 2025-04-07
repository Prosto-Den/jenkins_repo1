from framework.driver.driver import Driver
from framework.settings.configManipulator import ConfigManipulator
from framework.logger.logger import Logger
from test_data.dataManipulators import AlertDataManipulator, ProgressBarDataManipulator
import pytest


@pytest.fixture
def browser():
    AlertDataManipulator.init()
    ProgressBarDataManipulator.init()
    ConfigManipulator.init()
    Logger.init('logger', 'file.log', ConfigManipulator.data().level_log)
    Driver.init()

    yield

    Driver.close()
    AlertDataManipulator.clear()
    ProgressBarDataManipulator.clear()
    ConfigManipulator.clear()
