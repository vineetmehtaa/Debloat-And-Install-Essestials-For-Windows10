import webbrowser, subprocess
from os import system, name
from time import sleep

'''

Links that will go for downloads:

1. https://www.microsoft.com/en-us/p/bluetooth-audio-receiver/9n9wclwdqs5j#activetab=pivot:overviewtab
- Bluetooth Audio Receiver by Mark Smirnov

2. https://ninite.com/7zip-discord-firefox-foxit-malwarebytes-notepadplusplus-spotify-vscode-zoom/
- 7zip
- discord
- firefox
- malwarebytes
- notepad+
- spotify
- vscode
- zoom

3. https://protonvpn.com/download-windows
- Proton VPN 

4. iwr -useb https://git.io/debloat|iex
- Debloats windows through powershell
- Credits: https://github.com/Sycnex/Windows10Debloater
'''

# function to clear screen
def clear():
  
	# For windows
	if name == 'nt':
		clear = system('cls')
  
	# For mac and linux(here, os.name is 'posix')
	else:
		clear = system('clear')

# function to close the script
def check_script(choice):
	if "yY".find(choice) == -1:
		clear()
		print("Closing script now, thanks for using!")
		input("Enter any key to exit...")
		exit()

# displaying details
clear()
print("Welcome to the script!\n")
print("The following would be installed/executed:\n")
print(" 1. 7zip                       |   Igor Pavlov")
print(" 2. Bluetooth Audio Receiver   |   Mark Smirnov")
print(" 3. Discord                    |   Discord Inc.")
print(" 4. Firefox                    |   Mozilla Corporation")
print(" 5. Foxit PDF Reader           |   Foxit Software, Inc.")
print(" 6. Malwarebytes               |   Marcin Kleczynski")
print(" 7. Notepad++                  |   Don Ho")
print(" 8. ProtonVPN                  |   Proton Technologies AG")
print(" 9. Python3                    |   Guido van Rossum")
print("10. Spotify                    |   SPOTIFY TECHNOLOGY S.A.")
print("11. Visual Studio Code         |   Microsoft Corporation")
print("12. Windows_10_Debloater       |   Sycnex")
print("13. Zoom                       |   Zoom Video Communications, Inc.")
check_script(input("\nWould you like to continue[y/n] : "))

# opening links to go to websites for download
# NOTE: The applications from ninite can't be filtered individually
clear()
webbrowser.get().open("https://www.epicgames.com/store/en-US/download")
webbrowser.get().open("https://www.python.org/downloads/")
webbrowser.get().open("https://www.microsoft.com/en-us/p/bluetooth-audio-receiver/9n9wclwdqs5j#activetab=pivot:overviewtab")
webbrowser.get().open("https://ninite.com/7zip-discord-firefox-foxit-malwarebytes-notepadplusplus-spotify-vscode-zoom/")
webbrowser.get().open("https://protonvpn.com/download-windows")

# confirmation to debloat Windows 10
clear()
choice = input("Start Windows 10 Debloat? [y/n] : ")
if "yY".find(choice) > -1:
	subprocess.Popen("powershell -Command iwr -useb https://git.io/debloat|iex")
clear()