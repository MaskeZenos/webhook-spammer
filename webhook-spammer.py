from discord_webhook import DiscordWebhook
import os
def Main():
    os.system("cls")
    global num,webhooktkt,message
    print("Simple Webhook Spammer")
    print("Made by: MaskeZen945961 & PanSlunherOfficial")
    webhooktkt=input("Enter webhook: ")
    message=input("Enter message: ")
    num=input("Enter spam count: ")
    num=int(num)
    spam()

def spam():
    os.system("cls")
    for _ in range(num):
        webhook=DiscordWebhook(url=webhooktkt, content=message)
        webhook.execute()
    print("Finished Spamming!")
    input("Press Enter to continue...")
    Main()
Main()