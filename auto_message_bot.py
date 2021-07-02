def sendmessage():
    import requests
    import time
    from discord import Webhook, RequestsWebhookAdapter
    webhook = Webhook.from_url(
        'https://discord.com/api/webhooks/851983602756485171/FR2vH9C4l6VI2-LOghoLXDXWXBbHz1j-GLq_-8CO6x8mfEk2eOIhyOb4KHny2bfsv7yV',
        adapter=RequestsWebhookAdapter())
    webhook.send('Hello, how are you?')
    #time.sleep(10)

