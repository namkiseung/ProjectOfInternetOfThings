import scapy.contrib.mqtt as mqtt
pkt=IP(src='211.13.11.1', dst='192.168.43.59')
payload_packet=TCP(sport=9191, dport=1883, flags='S')
mqtt_pkt=mqtt.MQTTConnect(clientId='hacker')
reply, error = sr(pkt/payload_packer/mqtt_pkt, multi=1, timeout=1)
for x in reply:
	print(x[0].show2())
	
'''
import paho.mqtt.client as mqttClient
import time
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection
    else:
        print("Connection failed")
def on_message(client, userdata, message):
    print "Message received: "  + message.payload
Connected = False   #global variable for the state of the connection
broker_address= "192.168.43.6"  #Broker address
port = 1883                         #Broker port
user = "me"                    #Connection username
password = "abcdef"            #Connection password
client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
f = open('C:\Users\DELL\Desktop\workspace\MQTT연구\namkiseung\test.txt','w')
f.write('on_message')
f.close()
client.connect(broker_address, port=port)          #connect to broker
client.loop_start()        #start the loop
while Connected != True:    #Wait for connection
    time.sleep(0.1)
client.subscribe("/test")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop()
'''
'''
from scapy.contrib.mqtt import *
from scapy.all import send, sendp, IP, TCP, Ether, sr, sr1
seq = 12345
src='192.168.43.65'
dst='192.168.43.66'
sport = 1040
dport=1883
pkt=IP(src=src, dst=dst)   
SYN=pkt/TCP(sport=sport, dport=dport, flags="S")
SYNACK=sr1(SYN)
ACK=pkt/TCP(sport=sport, dport=dport, flags="A", seq=SYNACK.ack, ack=SYNACK.seq + 1)
send(ACK)
 
payload_packet = TCP(sport=sport, dport=dport, flags='A', seq=ACK.ack, ack=ACK.seq + 1)
mqtt_pkt = MQTTConnect(clientId='my_client_id')
reply, error = sr(pkt/payload_packet/mqtt_pkt, multi=1, timeout=1)
for r in reply:
    r[0].show2()
    r[1].show2()
'''