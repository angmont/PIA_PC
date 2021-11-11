#Socket para revisar puertos 
#Ayuda, se me habia olvidado el github JAJSJA SOS

import Socket

def checoPuertos(ip, portlist):
    try:
        for port in portlist:
            sock = socket.socket(socket.AF_NET,socket.SOCK_STREAM)
            sock.settimeout(7)
            result = sock.connect_ex((ip,port))
            if result == 0:
                print("Puerto {}: \t Abierto".format(port))
            else
                print("Puerto {}: \t Cerrado".format(port))
                
     except:
        pass
