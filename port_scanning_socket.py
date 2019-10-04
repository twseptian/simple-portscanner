#/usr/bin/python3 or higher

import os
import time
import argparse
from socket import *

startTime = time.time()

parser = argparse.ArgumentParser(description='port scanner')
parser.add_argument('-t', help='masukkan alamat ip target, berupa alamat IP, \
    maupun domain website', dest='target')
args = parser.parse_args()
target = args.target

def host(target):
    target_ip = gethostbyname(target)
    print('host: ', target_ip)

    return target_ip

def main():
    target_ip = host(target)
    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        connection = s.connect_ex((target_ip, i))
        if(connection == 0):
            print("port %d: OPEN"%(i,))
        s.close()
    print('time taken: ', time.time()-startTime)
if __name__ == "__main__":
    main()