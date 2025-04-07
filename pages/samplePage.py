from framework.pages.baseForm import BaseForm


class SamplePage(BaseForm):
    def __init__(self) -> None:
        super().__init__("//*[@id='sampleHeading']", 'Sample Page')
