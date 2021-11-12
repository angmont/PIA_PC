import socket
import sys

def checoPuertos(ip, portlist, puertoss):
  print("Empieza el escaneo de la ip: " + ip + " Con los puertos: " + puertoss)
  for port in portlist:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(7)
    result = sock.connect_ex((ip,port))
    if result == 0:
      print("Puerto {}: \t Abierto".format(port))
    else:
      print("Puerto {}: \t Cerrado".format(port))
  
