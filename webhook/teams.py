#Teams message card playground https://messagecardplayground.azurewebsites.net/
from .webhook import WebHookFormat

class Teams(WebHookFormat):
    def __init__(self) -> None:
        super().__init__()
        self.format = r"""{
            "@context": "http://schema.org/extensions",
            "@type": "MessageCard",
            "themeColor": "FF0000",
            "title": "$subject",
            "text": "$body",
            "potentialAction": [
                {
                "@type": "OpenUri",
                "name": "Open Link",
                "targets": [
                    { "os": "default", "uri": "$link" }
                ]
                }
            ]
        }"""