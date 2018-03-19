from socket import *

s = socket(AF_INET, SOCK_RAW, IPPROTO_TCP)

number = 1
while 1:
    print("Number: ", number)
    data = s.recvfrom(65565)
    packet = data[0]
    address = data[1]
    header = struct.unpack('!BBHHHBBHBBBBBBBB', packet[:20])
    if header[6] == 6:
        print("Protocol: TCP")
    elif header[6] == 17:
        print("Protocol: UDP")
    elif header[5] == 1:
        print("Protocol: ICMP") 
    print("Address: ", address)
    print("Data: ", data)
    number = number + 1
