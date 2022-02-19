from decouple import config
import requests
import sys
import json


def send_slack_message(message):
    url = config("SLACK_URL")
    title = f"Decoy Alert"
    slack_data = {
        "username": "Decoy",
        "attachments": [
            {
                "color": "#000000",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)