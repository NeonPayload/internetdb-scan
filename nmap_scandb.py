import nmap3
import sqlite3

nmap = nmap3.Nmap()

sqliteConnection = sqlite3.connect('shodanscan.db')
cursor = sqliteConnection.cursor()

#grabs all rows from database
scan_list_get = "SELECT * from shodanscan"
cursor.execute(scan_list_get)

#gets a list for a loop to nmap database
scan_list = cursor.fetchall()

print("Total items are: ", len(scan_list))
print("listing tables... \n")
# list of item in table for ref
#(ip, hostnames, cpes, ports, tags, vulns) 
for row in scan_list:
 print("ip: ", row[0])
 print("hostname: ", row[1])
 print("cpes: ", row[2])
 print("ports: ", row[3])
 print("tags: ", row[4])
 print("vulns: ", row[5])
 print("TESTING PORT STRING: " + row[3].strip())
 #strips and cleans ports info for scanning
 scan_port = row[3].strip()
 scan_port = scan_port.replace("[", "")
 scan_port = scan_port.replace("]", "")
 print(scan_port)
 #cleans up ip data for scanning
 scan_ip = row[0].strip()
 scan_ip = scan_ip.replace("[", "")
 scan_ip = scan_ip.replace("]", "")
 print(scan_ip)
# args isn't working correct for -p and pulling ports from db for now just scanning ip.
 print(nmap.nmap_list_scan(scan_ip))

 print("\n")
cursor.close()
