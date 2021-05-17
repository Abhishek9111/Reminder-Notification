import time
from plyer import notification
if __name__ == "__main__":
    while True:  
        notification.notify(
            title = "Please drink Water",                                           #this is the title for the notification
            message = "you need to stay hydrated to be efficient ",                 #type the message you want to be displayed with the notification
            timeout = 5                                                             
        )    
        time.sleep(60*60)
        
 #pythonw.exe .\main.py
 #type the above command in the terminal to fetch the current file into background process 

#app_icon = "F:\python\icon.ico",
#should be placed between message and timeout
#the above app icon can be replaced as per the demand and use of the user the image should be in ico format and the address for the
#image should be in ico format so that it can be properly utilized by the IDE, redirect to icon archieve website to grab other icons
#the app icon was removed to prevent errors in case of inavailability of file or incorrect directory of the ico file
