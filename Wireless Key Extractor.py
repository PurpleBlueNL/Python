###########################
# Wireless Key Extractor  #
# Made by E.Daemen        #
###########################

import subprocess
import os
import datetime

def WriteLog(): 
    Date = datetime.datetime.now()
    LogFile = open("WiFi_Export.txt","a")
    LogFile.write("#--------------------------------------------------------------------------\n")
    LogFile.write("# Datum:\t" + Date.strftime("%A-%d-%B-%Y") + "\n")
    LogFile.write("# Gebruiker:\t" + os.getlogin() + "\n# Computer:\t" + os.getenv('COMPUTERNAME')+"\n")
    LogFile.write("#--------------------------------------------------------------------------\n")
    LogFile.close()

# Get Wireless Profiles:
#----------------------------------
def Get_WiFi_Profiles():
    QueryData = subprocess.check_output(['netsh','wlan','show','profiles'])
    Data = QueryData.decode("utf-8")
    Data = Data.split("\n")
    SSIDs = []

    for ssid in Data:
        if "All User Profile" in ssid: 
            SSIDs.append((ssid.split(":")[1])[1:-1])
            
    return SSIDs

# Get Wireless Keys from profiles:
#----------------------------------    
def Get_WiFi_Keys():
    for SSID in Get_WiFi_Profiles() :
        QueryData = subprocess.check_output(['netsh','wlan','show','profile',SSID,'key=clear'])
        KeyData = QueryData.decode("utf-8")
        KeyData = KeyData.split("\n")
        Keys = []
        
        for key in KeyData:
            if "Key Conten" in key: 
                WiFiKey = key.split(":")[1]
                KeyFile = open("WiFi_Export.txt","a")
                KeyFile.write(SSID + " : " + WiFiKey)
                KeyFile.close()
                print(SSID+":"+WiFiKey)
     
    # Create empty lines
    KeyFile = open("WiFi_Export.txt","a")
    KeyFile.write("\n\n")
    KeyFile.close()


WriteLog()
Get_WiFi_Keys()
