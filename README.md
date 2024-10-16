# AES Encryption and Decryption

This project demonstrates AES encryption and decryption using Python. The server listens for encrypted messages from the client, decrypts them, and displays the decrypted message.

## How to Run

### 1. Start the Server
#### Use the following command to start the server:
```bash
python3 server.py <port number> <key>
```
* \<port number\>: The port number on which the server will listen.
* \<key\>: The 16-byte encryption key (e.g., abcdefghnbfghasd).

#### Example
```bash
python3 server.py 1234 abcdefghnbfghasd
```

### 2. Start the Client
#### Use the following command to start the client:
```bash
python3 client.py <server IP> <server port> <key>
```
* \<server IP\>: The IP address of the server.
* \<server port\>: The port number on which the server is listening.
* \<key\>: The same 16-byte encryption key as the server.

#### Example
```bash
python3 client.py 127.0.0.1 1234 abcdefghnbfghasd
```

### 3. Send Encrypted Message
Once the client is running, you can input any message in the terminal. 
The message will be sent encrypted using AES, and the server will decrypt it and display the original message

## Dependencies 
Make sure to have the following Python library installed:
```bash
sudo apt install python3-pip
sudo pip3 install pycryptodomex
```
