import scapy.all as scapy
import optparse

#1)arp_req
#2)broadcast
#3)response

def getUserInput():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ip",dest="ipAddress",help="Ip address that we need to find it's Mac Address")
    return parse_object.parse_args()

(ipToMac,arguments)=getUserInput()
if not ipToMac.ipAddress:
    print("Enter IP Address")

def netScanner(ipToMac):
    arpReqPacket = scapy.ARP(pdst=ipToMac)
    #scapy.ls(scapy.ARP())
    broadcastPacket=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combinedPacket = broadcastPacket/arpReqPacket  # Bu iki paketi al tek paket haline getir demek scapyde
    (answeredList,unansweredList) = scapy.srp(combinedPacket,timeout=1)
    answeredList.summary()
netScanner(ipToMac.ipAddress)
