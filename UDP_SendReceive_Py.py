import json
import socket
import time

# import sys, struct, random


localIP = "127.0.0.1"
receive_port = 20002
send_port_local = 20003
send_port_remote = 20004
bufferSize = 1024
udp_timeout = 0.5

# Create a datagram socket
udp_receiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_receiver.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, bufferSize)  # Limit the buffer to "bufferSize" bytes
udp_receiver.settimeout(udp_timeout)
udp_receiver.bind((localIP, receive_port))

# Create UDP Sender Socket
udp_sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_sender.bind(("127.0.0.1", send_port_local))
udp_sender.settimeout(udp_timeout)

# Print to show that the socket is ready to receive
print("UDP server up and listening")

# Listen for incoming datagrams
while True:
    time.sleep(0.5)
    try:
        bytesAddressPair = udp_receiver.recvfrom(bufferSize)
        msg = bytesAddressPair[0]
        address = bytesAddressPair[1]
        message_bites = "Message from LabVIEW (bite):{}".format(msg)
        message_utf8 = "Message from LabVIEW (string):{}".format(msg.decode())
        msg_parsed = json.loads(msg.decode("UTF-8"))
        msg_array = msg_parsed['Array']
        msg_string = msg_parsed['String']
        msg_numeric = msg_parsed['Numeric']
        msg_boolean = msg_parsed['Boolean']
    except socket.timeout as e:
        socket_timeout_error = e
        print(socket_timeout_error)
    else:
        print("------------Message received from LabVIEW------------------")
        print(message_bites)
        print(message_utf8)
        print(msg_array)
        print(msg_string)
        print(msg_numeric)
        print(msg_boolean)
        if not msg_boolean:
            break

    # Sending JSON to LabVIEW
    p_array = [113, 331, 313, 131]
    p_numeric = 333333
    p_string = "Hello from python"
    p_boolean = False
    py_msg = {
        "PArray": p_array,
        "PNumeric": p_numeric,
        "PString": p_string,
        "PBoolean": p_boolean
    }
    py_msg_json = json.dumps(py_msg)
    udp_sender.sendto(py_msg_json.encode("UTF-8"), (localIP, send_port_remote))

    print("------------Message being sent to LabVIEW------------------")
    print(py_msg)
    print(py_msg_json)
    # print(clientIP)
