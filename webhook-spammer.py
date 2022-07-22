from discord_webhook import DiscordWebhook


webhooktkt = input("Enter webhook: ")
message = input("Enter message: ")
    


def spamsa():
    while True:
        webhook = DiscordWebhook(url=webhooktkt, content=message)
        response = webhook.execute()
        spamsa()


spamsa()