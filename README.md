# Nutrimetics-Promo-ProductScraper
Extract Nutrimetics promo products automatically - to create a simple text file price list for customers

## Instructions - April 2017
Windows Instructions - Python, Selenium, Firefox, Beautifulsoup
- Install Python, if not installed already.
-	Install Anaconda (version used was Anaconda3-4.1.1-Windows-x86_64.exe)

o	Run cmd

o	Cd into the Anaconda directory

-	Need to install selenium module

o	$ pip install –U selenium

o	If Selenium 3 is installed :

-	download geckodriver from https://github.com/mozilla/geckodriver/releases for your OS. Unzip the downloaded file and keep it in one of your project folder (ie. D:\ drive or Python path). Now set the path to geckodriver as a system path property manually in Windows. 

Search for PATH

Environment variables – system

Add geckodriver to System PATH variable (directory goes at end of list)

Reboot Windows
-	$ pip install beautifulsoup4
-	Install and setup Firefox (see Setup Section below) to work with Selenium
-	Put the Python script file Python_Nutrispace_Login_OnPromotion_UserInput.py into a directory on the computer
-	Create a Batchfile, put it on the desktop, so the script User can run the script directly from the Windows Desktop

## Setup Firefox
### How to create Firefox profile for your Selenium?
1. Make sure all your firefox instance are closed
2. Click Start>Run
3. Type “firefox.exe -ProfileManager -no-remote”
4. Select “Create Profile” (i.e. selenium)
5. Click “Next”
6. Enter new profile name
7. Select a directory folder to store your new profile
8. Click “Finish”
9. Select “Don’t ask at startup”
10. Click “Start Firefox” and configure settings based on suggestion below***
11. Set Profile back to “default” (enable you to use your previous settings on your browser)
12. Add -firefoxProfileTemplate command line option as you start the Selenium Server
java -jar selenium-server.jar -firefoxProfileTemplate “<Selenium Profile Directory>”
  
### Suggested settings for your Selenium Profile
1.From “Menu –View - Toolbars” tab, uncheck “Bookmarks Toolbar”.

2.Right click from toolbar and click “Customize”

3.Remove “Google search” by dragging it to the “Customize Toolbar” window

4.Exit Customize.

5.Click “Options” then set the following:

 a. “Main” Tab
 
 – set Home Page to “about:blank”
 
 b. “Tabs” option
 
 – Select “a new window” for new pages
 
c. “Content” tab

 – uncheck “Block pop-up” windows option
 
 d. “Privacy” tab
 
 – uncheck all “History” options – if restart then Win+R – “firefox.exe -ProfileManager -no-remote” in admin mode - use Firefox profile selenium and add settings to it.
 
 e. “Security” tab
 
 – uncheck all “Security” options
 
 – click “Settings” and uncheck all warning options
 
 f. “Advanced” tab
 
 – Uncheck “autoscrolling” option from “General” tab
 
 – uncheck “warn me …” and “Search Engines”option from “Update” tab
 
6. From the address bar type “about:config” and add the following by right-click anywhere on the page and selecting “new”
 – extensions.update.notifyUser (type=boolean; value=false)
 
 – extensions.newAddons (type=boolean; value=false)
 
-	security.insecure_field_warning.contextual.enabled. 

and

-	security.insecure_password.ui.enabled

Double-click each  to change their values to false.

7. From “Tools\Add-ons” install the following:
 – Firebug: allows you to edit, debug, and monitor CSS, HTML, and JavaScript on your application under test
 – Selenium IDE: allows you to record, edit, and debug Selenium tests
 – ScreenGrab: saves entire webpages as images.
