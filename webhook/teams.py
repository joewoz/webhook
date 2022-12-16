# Teams message card playground https://messagecardplayground.azurewebsites.net/
# New Designer https://amdesigner.azurewebsites.net/
# Designer for more options https://www.adaptivecards.io/designer/
# Docs on how to wrap the card as attachment https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/connectors-using?tabs=cURL#send-adaptive-cards-using-an-incoming-webhook
from .webhook import WebHookFormat

class Teams(WebHookFormat):
    def __init__(self) -> None:
        super().__init__()
        self.format = r"""{
            "type":"message",
            "attachments":[
                {
                    "contentType":"application/vnd.microsoft.card.adaptive",
                    "contentUrl":null,
                    "content":{
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                        "type": "AdaptiveCard",
                        "version": "1.0",
                        "@type": "AdaptiveCard",
                        "@context": "http://schema.org/extensions",
                        "body": [
                            {
                                "type": "Container",
                                "id": "4b7f667c-d017-5ed1-17c4-7e9e50375a12",
                                "padding": "None",
                                "items": [
                                    {
                                        "type": "TextBlock",
                                        "id": "SUBJECT_CONTAINER",
                                        "text": "$subject",
                                        "wrap": true,
                                        "size": "Large",
                                        "weight": "Bolder"
                                    },
                                    {
                                        "type": "ColumnSet",
                                        "columns": [
                                            {
                                                "type": "Column",
                                                "id": "58d15e62-648c-2458-7990-704fccb5f1fe",
                                                "padding": "None",
                                                "width": "50px",
                                                "items": [
                                                    {
                                                        "type": "TextBlock",
                                                        "id": "SOURCE_CONTAINER",
                                                        "text": "$source",
                                                        "wrap": true,
                                                        "size": "Large",
                                                        "weight": "Bolder",
                                                        "horizontalAlignment": "Right"
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "Column",
                                                "id": "19cb8c0d-68df-3a54-2218-1c88394ba01e",
                                                "padding": "None",
                                                "width": "stretch",
                                                "items": [
                                                    {
                                                        "type": "TextBlock",
                                                        "id": "BODY_CONTAINER",
                                                        "text": "$body",
                                                        "wrap": true
                                                    },
                                                    {
                                                        "type": "ActionSet",
                                                        "id": "ACTION_CONTAINER",
                                                        "actions": [
                                                            {
                                                                "type": "Action.OpenUrl",
                                                                "id": "77b624e1-b1bd-2444-1cdd-0d4a642e875c",
                                                                "title": "Open Link",
                                                                "url": "$link",
                                                                "style": "positive",
                                                                "isPrimary": true
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ],
                                        "padding": "None",
                                        "separator": true
                                    }
                                ]
                            }
                        ],
                        "padding": "Small"
                    }
                }
           ]
        }
        """
