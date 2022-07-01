#Chime webhooks doc https://docs.aws.amazon.com/chime/latest/ug/webhooks.html
from .webhook import WebHookFormat

class Chime(WebHookFormat):
    def __init__(self) -> None:
        super().__init__()
        self.format = r"""{"Content": "${subject}\n\n${body}\n\n${link}"}"""