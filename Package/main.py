import tutorial

json_data = {
    "content": "Hello :)",
    "username": "Llama Dude"
}

print(tutorial.webhookSend("https://discord.com/api/webhooks/",
                           json_data))
