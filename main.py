# import SimpleHTTPServer
# import SocketServer
import os
import logging
import sys
import readOptions

# Port that's open
PORT = readOptions.getOptions('options_honeypot', 'port')
print(f"Port: {PORT}")

# Pretty sure this doesn't work with syslog FIX: change later
logging.basicConfig(
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO,
    filename = 'honeypot.log',
)
