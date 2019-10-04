#/usr/bin/python3 or higher

import os
import time
import argparse
import nmap
from socket import *

startTime = time.time()

parser = argparse.ArgumentParser(description='port scanner')
parser.add_argument('-t', help='masukkan alamat ip target, berupa alamat IP, \
    maupun domain website', dest='target')
parser.add_argument('-p', help='range port, contoh: 21-111', dest='ports')
args = parser.parse_args()
target = args.target
ports = args.ports

def host_target(target, ports):
    nmapScan = nmap.PortScanner()
    target_ip = gethostbyname(target)
    nmapScan.scan(target_ip, ports)
    print('host: %s dengan range target port %s'%(target_ip, ports))
    
    return nmapScan, target_ip

def main():
    nmapScan, target_ip = host_target(target, ports)
    for host in nmapScan.all_hosts():
        print('Host : %s (%s)' % (host, nmapScan[host].hostname()))
        print('State : %s' % nmapScan[host].state())
        for proto in nmapScan[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            lport = nmapScan[host][proto].keys()
            for port in lport:
                print('port : %s state : %s'%(port, nmapScan[host][proto][port]['state']))
                
    print('time taken: ', time.time()-startTime)
    
if __name__ == "__main__":
    main()