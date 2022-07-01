#Slack message builder https://api.slack.com/docs/messages/builder
from .webhook import WebHookFormat

class Slack(WebHookFormat):
    def __init__(self) -> None:
        super().__init__()
        self.format = r"""{
            "text": "*${subject}*\n\n${body}\n\n<${link}|Link>",
            "username": "SlackBot",
            "mrkdwn": true
        }"""