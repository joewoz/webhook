"""WebHook Library"""
from .discord import Discord
from .chime import Chime
from .slack import Slack
from .teams import Teams
from .webhook import WebHook, MockResponse, mock_post_fn, WebHookFormat