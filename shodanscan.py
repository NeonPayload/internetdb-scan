import sqlite3
import json
import requests

#TODO we can now put ip's in database, now use for loop to grab hosts from txt // done
#TODO find a way to scan what is in database (maybe new script?) 
#TODO for scanning, you will need to strip the [] and the '' away for nmap library to work. when pulling from the database


conn = sqlite3.connect('shodanscan.db')
cursor = conn.cursor()
#below line creates shodan table commented it out to not cause errors 
#conn.execute("CREATE TABLE shodanscan (ip text, hostnames text, cpes text, ports text, tags text, vulns text);")

# find better way to do this
print("NOTE: please use list of IP's hostname usually don't work with internetdb. \n")
hostfile = input("Enter hostname file: ")
try:
   list_of_hosts = open(hostfile, "r")
except FileNotFoundError:
   print("error not able to open file or not there")
except IOError:
   print("file cannot open")
         
for line in list_of_hosts:
#   print("[debug]printing line " + line) 
   ip = line.strip()
   print("https://internetdb.shodan.io/" + ip)
   data = requests.get("https://internetdb.shodan.io/"+ ip).json()
   try:
      print(data)
      print(str(data["hostnames"]) + "being placed into database")
      # below line places everything into database I don't know why it wasn't being pulled as a string but oh well.
      cursor.execute("INSERT INTO shodanscan (ip, hostnames, cpes, ports, tags, vulns) VALUES (?, ?, ?, ?, ?, ?)", (str(data["ip"]), str(data["hostnames"]), str(data["cpes"]), str(data["ports"]), str(data["tags"]), str(data["vulns"])))
      print("Inserted into database.\n")

   except:
      print("could not grab data for: " + line)
      #cursor.execute("""INSERT INTO shodanscan (ip, hostnames, cpes, ports, tags, vulns) VALUES (?, ?, ?, ?, ?, ?)", (data["ip"], data["hostnames"], data["cpes"], data["ports"], data["tags"], data["vulns"])""")
   


conn.commit()
conn.close()
