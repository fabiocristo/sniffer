from socket import *

s = socket(AF_INET, SOCK_RAW, IPPROTO_TCP)

n = 1
while 1:
    print('Number ', n)
    data = s.recvfrom(65565)
    packet = data[0]
    address = data[1]
    header = struct.unpack('!BBHHHBBHBBBBBBBB', packet[:20])
    if header[6] == 6:
        print("Protocolo: TCP")
    elif header[6] == 17:
        print("Protocolo: UDP")
    elif header[5] == 1:
        print("Protocolo: ICMP") 
    print("Address: ", address)
    print("Data: ", data)
    n = n + 1
