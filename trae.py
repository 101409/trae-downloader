import requests
import platform 
from colorama import Fore
import os

# download urls for Windows and Mac
win_url = "https://lf-cdn.trae.ai/obj/trae-ai-us/pkg/app/releases/stable/1.0.10283/win32/Trae-Setup-x64.exe"
mac_url = "https://lf-cdn.trae.ai/obj/trae-ai-us/pkg/app/releases/stable/1.0.10282/darwin/Trae-darwin-x64.dmg"

if (platform.system() == "Windows"):
    url = win_url
    filename = "Trae-Setup-x64.exe"
    download_path = os.path.join(os.path.expanduser("~"), "Downloads", filename)
    print(Fore.BLUE + "[+] "+ Fore.RESET + "Downloading" + Fore.RED + " Trae" + Fore.RESET + ", Windows version.")
else:
    url = mac_url
    filename = "Trae-darwin-x64.dmg"
    download_path = os.path.join(os.path.expanduser("~"), "Downloads", filename)
    print(Fore.BLUE + "[+] "+ Fore.RESET + "Downloading" + Fore.RED + " Trae" + Fore.RESET + ", Mac version.")

# download file
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(download_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
    print(Fore.GREEN + "[✔] " + Fore.RESET + f"Download complete: {download_path}")
else:
    print(Fore.RED + "[✘] " + Fore.RESET + "Download failed. Check the URL.")