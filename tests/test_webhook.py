import logging
import webhook
import pytest
from requests.exceptions import ConnectionError

class MockThrottleResponse:
    status_code: int = 429
    headers: dict = {'Content-Type': 'Application/JSON'}
    text: str = ""

class MockAuthFailResponse:
    status_code: int = 401
    headers: dict = {'Content-Type': 'Application/JSON'}
    text: str = ""

def mock_post_throttle(url: str, data="", headers=None) -> MockThrottleResponse:
    logging.info(f"MOCK_SEND_FUNCTION: \nURL:{url}\nDATA:{data}\nHEADERS:{headers}")
    return MockThrottleResponse()

def mock_post_auth_fail(url: str, data="", headers=None) -> MockAuthFailResponse:
    logging.info(f"MOCK_SEND_FUNCTION: \nURL:{url}\nDATA:{data}\nHEADERS:{headers}")
    return MockAuthFailResponse()

def mock_post_raise_exception(url: str, data="", headers=None):
    logging.info(f"MOCK_SEND_FUNCTION: \nURL:{url}\nDATA:{data}\nHEADERS:{headers}")
    raise(Exception("Some random error"))

def mock_post_connection_exception(url: str, data="", headers=None):
    logging.info(f"MOCK_SEND_FUNCTION: \nURL:{url}\nDATA:{data}\nHEADERS:{headers}")
    raise(ConnectionError())

@pytest.fixture()
def connection_exception_raised_handler():
    return webhook.WebHook("http://example.com", webhook.Slack, post_funct=mock_post_connection_exception)

@pytest.fixture()
def exception_raised_handler():
    return webhook.WebHook("http://example.com", webhook.Slack, post_funct=mock_post_raise_exception)

@pytest.fixture()
def throttle_handler():
    return webhook.WebHook("http://example.com", webhook.Slack, post_funct=mock_post_throttle)

@pytest.fixture()
def auth_fail_handler():
    return webhook.WebHook("http://example.com", webhook.Slack, post_funct=mock_post_auth_fail)

@pytest.fixture()
def chime_handler():
    return webhook.WebHook("http://example.com", webhook.Chime, post_funct=webhook.mock_post_fn)

@pytest.fixture()
def teams_handler():
    return webhook.WebHook("http://example.com", webhook.Teams, post_funct=webhook.mock_post_fn)

@pytest.fixture()
def discord_handler():
    return webhook.WebHook("http://example.com", webhook.Discord, post_funct=webhook.mock_post_fn)

@pytest.fixture()
def slack_handler():
    return webhook.WebHook("http://example.com", webhook.Slack, post_funct=webhook.mock_post_fn)

@pytest.fixture()
def no_url_handler():
    return webhook.WebHook("", webhook.Slack, post_funct=webhook.mock_post_fn)

def test_webhook_slack(slack_handler: webhook.WebHook):
    slack_handler.send("TESTING", "Testing Slack Bot Again.. ignore this", "n/a")

def test_webhook_chime(chime_handler: webhook.WebHook):
    chime_handler.send("TESTING", "Testing Chime Bot Again.. ignore this", "n/a")

def test_webhook_discord(discord_handler: webhook.WebHook):
    discord_handler.send("TESTING", "Testing Discord Bot Again.. ignore this", "n/a")

def test_webhook_teams(teams_handler: webhook.WebHook):
    teams_handler.send("TESTING", "Testing Teams Bot Again.. ignore this", "n/a")

def test_mock_throttle(throttle_handler: webhook.WebHook):
    with pytest.raises(Exception):
        throttle_handler.send("TESTING", "Testing mock throttle event", "n/a")

def test_mock_auth_fail(auth_fail_handler: webhook.WebHook):
    resp = auth_fail_handler.send("TESTING", "Testing mock throttle event", "n/a")
    assert resp is False

def test_exception_raised(exception_raised_handler: webhook.WebHook):
    resp = exception_raised_handler.send("TESTING", "Testing mock raise error event", "n/a")
    assert resp is False

def test_connection_error(connection_exception_raised_handler: webhook.WebHook):
    resp = connection_exception_raised_handler.send("TESTING", "Testing mock raise connection error event", "n/a")
    assert resp is False

def test_no_url(no_url_handler: webhook.WebHook):
    resp = no_url_handler.send("TESTING", "Testing no URL event", "n/a")
    assert resp is False