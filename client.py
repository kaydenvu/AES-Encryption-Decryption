import socket
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

# Server's IP address
SERVER_IP = "127.0.0.1"

# The server's port number
SERVER_PORT = 1235

# The client's socket
cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attempt to connect to the server
cliSock.connect((SERVER_IP, SERVER_PORT))

# The AES block size must always be 16 bytes
BLOCK_SIZE = 16

# Encryption key (for AES must be 16, 24, or 32 bytes!)
ENCRYPTION_KEY = b'Sixteen byte key'

# The key (must be 16 bytes)
key = ENCRYPTION_KEY

# Set up the AES encryption class
encCipher = AES.new(key, AES.MODE_ECB)

# Send the message to the server
msg = input("Please enter a message to send to the server: ")

# Convert the message to bytes
plainBytes = msg.encode('utf-8')

# Pad the plaintext to make it a multiple of BLOCK_SIZE
padded_plainBytes = pad(plainBytes, BLOCK_SIZE)

# Encrypt the padded plaintext
cipherBytes = encCipher.encrypt(padded_plainBytes)

# Send the message to the server
# NOTE: the user input is of type string
# Sending data over the socket requires.
# First converting the string into bytes.
# encode() function achieves this.
cliSock.send(cipherBytes)

