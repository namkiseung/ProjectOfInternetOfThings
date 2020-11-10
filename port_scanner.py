import argparse
from scapy.all import *

def print_ports(port, state):
	print("%s | %s" % (port, state))
#syn scan
def syn_scan(target, ports):
	print("[+] syn scan on, %s with ports %s" % (target, ports))
	sport = RandShort()
	for port in ports:
		pkt = sr1(IP(dst=target)/TCP(sport=sport, dport=port, flags="S"), timeout=1, verbose=0)
		if pkt != None:
			if pkt.haslayer(TCP):
				if pkt[TCP].flags == 20:
					print_ports(port, "Closed")
				elif pkt[TCP].flags == 18:
					print_ports(port, "Open")
				else:
					print_ports(port, "TCP packet resp | filtered")
			elif pkt.haslayer(ICMP):
				print_ports(port, "ICMP resp | filtered")
			else:
				print_ports(port, "Unknown resp")
				print(pkt.summary())
		else:
			print_ports(port, "Unanswered")

# udp scan
def udp_scan(target, ports):
	print("[+] udp scan on, %s with ports %s" % (target, ports))
	for port in ports:
		pkt = sr1(IP(dst=target)/UDP(sport=port, dport=port), timeout=2, verbose=0)
		if pkt == None:
			print_ports(port, "Open | filtered")
		else:
			if pkt.haslayer(ICMP):
				print_ports(port, "Closed")
			elif pkt.haslayer(UDP):
				print_ports(port, "Open | filtered")
			else:
				print_ports(port, "Unknown")
				print(pkt.summary())

# xmas scan
def xmas_scan(target, ports):
	print("[+] Xmas scan on, %s with ports %s" %(target, ports))
	sport = RandShort()
	for port in ports:
		pkt = sr1(IP(dst=target)/TCP(sport=sport, dport=port, flags="FPU"), timeout=1, verbose=0)
		if pkt != None:
			if pkt.haslayer(TCP):
				if pkt[TCP].flags == 20:
					print_ports(port, "Closed")
				else:
					print_ports(port, "TCP flag %s" % pkt[TCP].flag)
			elif pkt.haslayer(ICMP):
				print_ports(port, "ICMP resp | filtered")
			else:
				print_ports(port, "Unknown resp")
				print(pkt.summary())
		else:
			print_ports(port, "Open | filtered")

parser = argparse.ArgumentParser("Port scanner using Scapy")
parser.add_argument("-t", "--target", help="대상 IP", required=True)
parser.add_argument("-p", "--ports", type=int, nargs="+", help="")
parser.add_argument("-s", "--scantype", help="한 개 선택 syn/udp/xmas", required=True)
args = parser.parse_args()

target = args.target
scantype = args.scantype.lower()

if args.ports:
	ports = args.ports
else:
	ports = range(1, 1024)

if scantype == "syn" or scantype == "s":
	syn_scan(target, ports)
elif scantype == "udp" or scantype == "u":
	udp_scan(target, ports)
elif scantype == "xmas" or scantype == "x":
	xmas_scan(target, ports)
else:
	print("[+] 타입 잘못씀")