import os 
hostname = input('Enter the IP address:') 
response = os.system("ping -c 1 " + hostname)  

if response == 0:   
      print (hostname, 'Reboot successful!')
else:
      print (hostname, 'Rebooting..!')