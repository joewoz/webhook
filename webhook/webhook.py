import logging
import os
import requests
from string import Template

logging.basicConfig()
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')  # Default to INFO
internal_logger = logging.getLogger('webhook')
internal_logger.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))

class WebHookFormat:
    """Base Class for Web Hook Format Strings"""
    format: str

    def format_message(self, args={}):
        """Will return full message format with included arguments"""
        format_template = Template(self.format)
        return format_template.safe_substitute(args)


class WebHook():
    """Main webhook class - instanciate this and call the send function"""
    def __init__(self, url: str, format: WebHookFormat, logger=internal_logger, post_funct=requests.post) -> None:
        self.url = url
        self.format = format() # Need to call the class to create an instance of it
        self.log = logger
        self.post = post_funct
    
    def send(self, subject: str, body: str, link: str):
        """Sends a message to the webhook's configured URL"""
        if self.url:
            HEADERS = {"Content-Type": "application/json"}
            message = self.format.format_message(
                args={
                    'subject': subject,
                    'body': body,
                    'link': link
                }
            )
            try:
                self.log.info("Now attempting to call Webhook API for message '{}'".format(subject))
                response = self.post(
                    self.url,
                    data=message,
                    headers=HEADERS
                )
            except requests.exceptions.ConnectionError as ce:
                self.log.error("Connection Error: {}".format(ce))
                return False
            except Exception as other_error:
                self.log.error("Some other kind of error happened: {}{}".format(
                    type(other_error).__name__,
                    str(other_error.args)
                ))
                return False
            if response.status_code == 429:
                raise Exception("Webhook request throttled")
            if response.status_code > 299: 
                self.log.error('Sent Message:{} Status:{} Headers: {} Error Response: {}'.format(message, response.status_code, response.headers, response.text))
                return False
            else:
                self.log.info('Message sent successfully (STATUS:{})'.format(response.status_code))
            return True
        else:
            self.log.info("WEBHOOK: No Webhook URL has been defined")
            return False

class MockResponse:
    """Example response which mocks the requests library's Response object"""
    status_code: int = 200
    headers: dict = {'Content-Type': 'Application/JSON'}
    text: str = ""

def mock_post_fn(url: str, data="", headers=None) -> MockResponse:
    """Example function you can use as the post_funct argument to mock the webhook action"""
    internal_logger.info(f"MOCK_SEND_FUNCTION: \nURL:{url}\nDATA:{data}\nHEADERS:{headers}")
    return MockResponse()

