import os
import time
import requests
import getpass
from colorama import Fore
from pystyle import Center

os.system("cls" if os.name == "nt" else "clear")
if os.name == "nt":
	os.system("title Hypesquad changer - spy404#6985")
token = getpass.getpass(prompt = f"{Fore.GREEN} Token: ")
choice = input("[1] - Bravery \n[2] - Briliance \n[3] - Balance \n>>> ")
headerpost = {
	'Authorization': token
}
payloads = {
	'house_id': choice
}
time.sleep(1)
requests.session().post("https://discord.com/api/v8/hypesquad/online", json=payloads, headers=headerpost)
print(Center.XCenter("You're badge successfuly changed!"))
print(Center.XCenter("Developed with love by spy404"))
