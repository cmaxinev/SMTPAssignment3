from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    if recv[:3] != '220':
        #print('220 reply not received from server.')
    # Fill in end

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start

    mailFromCommand = "MAIL FROM: <cv2125@nyu.edu> \r\n"
    clientSocket.send(mailFromCommand.encode())
    recv1 = clientSocket.recv(1024)
    #print(recv1)

    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start

    rcptToCommand = 'RCPT TO: <vasquez.chanelle@gmail.com> \r\n'
    clientSocket.send(rcptToCommand.encode())
    recv1 = clientSocket.recv(1024)
    #print(recv1)

    # Fill in end

    # Send DATA command and print server response.
    # Fill in start

    dataCommand = 'DATA\r\n'
    #print (dataCommand)
    clientSocket.send(dataCommand.encode())
    recv1 = clientSocket.recv(1024)
    #print(recv1)

    # Fill in end

    # Send message data.
    # Fill in start

    mailMessageEnd = '\r\n.\r\n'
    message = msg + mailMessageEnd
    clientSocket.send(message.encode())
    recv1= clientSocket.recv(1024)
    #print(recv1)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start

    quitCommand = 'QUIT\r\n'
    #print(quitCommand)
    clientSocket.send(quitCommand.encode())
    recv1 = clientSocket.recv(1024)
    clientSocket.close()
    #print(recv1)

    # Fill in end

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
