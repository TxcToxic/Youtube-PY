# This is to send data to a Webhook from Discord!

import pwgen
import _base64
import requests
import time

url = "https://discord.com/api/webhooks/1045398616371634176/wbwkzxGpNe_OTOuDnzt-Mk-Pnpspf7shV5DPJ_Fi7jJSomJHKrb8-C3KPAtFvctu5NiO"

data = {
    "content": None,
    "username": "Webhook.py - CFT-Development",
    "embeds": [
        {
            "title": "Password",
            "description": "Source made by -TOXIC-#1835",
            "fields": [
                {
                    "name": "Password - Encoded:",
                    "value": f"`{_base64.encode(str(pwgen.genPwd(32)))}`"
                },
                {
                    "name": "Generated at:",
                    "value": f"{time.strftime('%T -- %D')}"
                }
            ]
        }
    ]
}

print(requests.post(url=url, json=data).status_code)
