import logging
import socket
import readOptions

# Pretty sure this doesn"t work with syslog FIX: change later
# Sets up logging settings
logging.basicConfig(
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
    filename = "honeypot.log",
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Local IP/Port for the honeypot to listen on (TCP)
LOCAL_HOST = '0.0.0.0'
# Gets port from options.ini file (should be able to switch between ssh and telnet)
LOCAL_PORT = int(readOptions.getOptions("options_honeypot", "port"))

# Remote IP/Port to send the log data to (TCP)
# FIX:
LOG_HOST = ""
LOG_PORT = 9000

# Banner displayed when connecting to the honeypot
BANNER = "Ubuntu 18.04 LTS\nlogin: "
# Socket timeout in seconds
TIMEOUT = 10


# TODO: Rename s
def main():
    # Sets up the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((LOCAL_HOST, LOCAL_PORT))
    # Waiting for connection
    s.listen(100)
    while True:
        print("Honeypot is waiting connections...")
        clientsocket, clientaddress = s.accept()
        s.settimeout(TIMEOUT)
        logger.info(f"{clientsocket} has connected at {clientaddress}")
        print(f"Honeypot has connection from {clientaddress}")
        try:
            clientsocket.send(bytes(BANNER, "utf-8"))
            msg = s.recv(1024)
        except socket.error as e:
            logger.critical(f"Error: {str(e)}")
        else:
            logger.critical(f"Data: {msg}")
        finally:
            s.close()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
