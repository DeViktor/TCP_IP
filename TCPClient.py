from logging import exception
import socket
import sys

def main():
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
  except socket.error as e:
    print("error{}".format(e))
    sys.exit()
  
  print("socket as been created")
  
  host = input("hostname or IP ")
  port = int(input("Port "))
  
  try:
    s.connect((host, port))
    print("sucess")
    s.shutdown(2)
  except socket.error as e:
    print("error{}".format(e))
    sys.exit()

if __name__ =="__main__":
  main()