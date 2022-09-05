import scoket
import sys 
import time

usage ="python3 port_scanner.py TARGET START_PORT END PORT"

print ("-"*50)
print ("python simple port scanning")
print ("-"*50)

if(len(sys.argv)!= 4):
    print(usage)
    sys.exit()

    try:19
        target = socket.gethostbyname (sys.argv[1])
        except sockket.gaierror:
            print ("Name resolution error")
            
           sys.exit()

    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    for port in range (start_port,end_port+1):
        
        s = socket.scoket (socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect ((target,port))
        if (not conn):
            print("port {} is OPEN". format (port))
            s.close() 