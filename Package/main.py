import tutorial

json_data = {
    "content": "Hello :)",
    "username": "Llama Dude"
}

print(tutorial.webhookSend("https://discord.com/api/webhooks/1055411133432987668/oIB_wSkg1TvZcoMsezyFSrOVuT9ob9kfMxtHuK0kmSbFmDSfOlzE33G7N741fJEN2o3L",
                           json_data))
