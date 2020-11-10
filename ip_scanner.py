from scapy.all import *
import sys, argparse

s=[]

parser = argparse.ArgumentParser("IP scanner using Scapy")
parser.add_argument("-t", "--target", help="대상 IP 대역. ex) 192.168.0", required=True)
args = parser.parse_args()

target = args.target

for i in range(1,255):
	arp_req=Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=target+"."+str(i))
	arp_ans=srp1(arp_req, timeout=0.5)
	if arp_ans:
		s.append(str(target+"."+str(i)+" is at "+arp_ans[ARP].hwsrc))

for j in range(0,len(s)):
	print(s[j])
