import socket
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad

####### A SIMPLE ILLUSTRATION OF THE TCP SERVER #######

# The port number on which to listen for incoming
# connections.
PORT_NUMBER = 1235

# Create a socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Associate the socket with the port
serverSock.bind(('', PORT_NUMBER)) 

# Start listening for incoming connections (we can have
# at most 100 connections waiting to be accepted before
# the server starts rejecting new connections)
serverSock.listen(100)

# The AES block size must always be 16 bytes
BLOCK_SIZE = 16

# Encryption key (for AES must be 16, 24, or 32 bytes!)
ENCRYPTION_KEY = b'Sixteen byte key'

# The key (must be 16 bytes)
key = ENCRYPTION_KEY

# Set up the AES encryption class
decCipher = AES.new(key, AES.MODE_ECB)

# Keep accepting connections forever
while True:

	print("Waiting for clients to connect...")
	
	# Accept a waiting connection
	cliSock, cliInfo = serverSock.accept()
	
	print("Client connected from: " + str(cliInfo))
	
	# Receive the data the client has to send.
	# This will receive at most 1024 bytes
	cliMsg = cliSock.recv(1024)

	print("Client sent " + str(cliMsg))
	#Decrypt the message.
	decryptedText = decCipher.decrypt(cliMsg)

	#Unpad the text using BLOCK_SIZE
	unpaddedText = unpad(decryptedText, BLOCK_SIZE) 

	print("Decrypted text: " + unpaddedText.decode('utf-8'))

	
	# Hang up the client's connection
	cliSock.close()
