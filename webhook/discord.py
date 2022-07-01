from .webhook import WebHookFormat

class Discord(WebHookFormat):
    """Discord Webhook Format Defintion"""
    def __init__(self) -> None:
        super().__init__()
        self.format = r"""{
            "content": "${body}",
            "tts": true
        }"""