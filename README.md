# WebHook Module
This module allows easy use and extensibility for invoking webhooks across different types of messaging systems.

## Use

Example to send a message to a discord webhook
```python
import webhook
URL = "https://discord.com/api/webhooks/xyz"
wh = webhook.WebHook(URL, webhook.Discord)
wh.send("TESTING", "Testing Discord...", "n/a")
```
1. Import the webhook module
2. Create an instance of the WebHook class
    a. Specify the webhook URL
    b. Sepcify the format by calling the specific format class, in this case Discord


## Testing using mock web post function
To test the send function without actually sending the message, simply specify a different post function.

In the following example, we use the built-in mock_post_fn to do this
```python
wh = webhook.WebHook(URL, webhook.Discord, post_funct=webhook.mock_post_fn)
```

## Extendability - Format Classes
This module current comes with some out-of-the box format classes for Chime, Discord, Slack and Teams. You can easily modify these by editing the class directly in the module or creating a new format class inherited from the `webhook.WebHookFormat` base class. 

When you create a new format class, you simply just need to set the `format` instance variable to a string that contains the format string (using `${}` substitution) which will be processed by the standard `Tempalate.safe_substitute` function.  Use one of the example format classes as an example.


### If your webhook platform doesn't support HTTP post method
If for some reason the platform you want to send a message to does not use the HTTP post method but rather some other kind of method, you can use the post_funct parameter to pass along any other kind of function that accepts a positional first agrument for the URL, and `data` and `headers` named arguments.

## Environment / Requirements
This environment uses Pipenv and Pipfile to manage Python dependencies

Run `pipenv install` to install the dependencies

Run `pipenv shell` to load the virtual environment


## Tests

Run `pytest --cov --cov-report html` to get a nice HTML coverage report
