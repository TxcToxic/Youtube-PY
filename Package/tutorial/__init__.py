import requests
import json


def webhookSend(url, raw_json_payload):
    data = json.dumps(raw_json_payload)
    response = requests.post(url, data=data, headers={"Content-Type": "application/json"})
    return "Status: {} // 200/204 means everything worked!".format(response.status_code)
