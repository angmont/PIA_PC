import socket
import sys
import logging

def checoPuertos(ip, portlist, puertoss):
  logging.info("Se entró a la funcion \"checoPuertos\" ")
  logging.info("Empieza el escaneo de la ip: " + ip + " Con los puertos: " + puertoss)
  print("Empieza el escaneo de la ip: " + ip + " Con los puertos: " + puertoss)
  for port in portlist:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(7)
    result = sock.connect_ex((ip,port))
    if result == 0:
      print("Puerto {}: \t Abierto".format(port))
      logging.info("Puerto {}: \t Abierto".format(port))
    else:
      print("Puerto {}: \t Cerrado".format(port))
      logging.info("Puerto {}: \t Cerrado".format(port))
