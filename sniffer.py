from socket import *

s = socket(AF_INET, SOCK_RAW, IPPROTO_TCP)

while 1:
  print(s.recvfrom(65565).decode())
