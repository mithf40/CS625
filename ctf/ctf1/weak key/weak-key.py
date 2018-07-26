import socket

PORT = 8030
HOSTNAME = 'cseproj91.cse.iitk.ac.in'

def netcat(text_to_send):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(( HOSTNAME, PORT ))
    s.sendall(text_to_send)
    s.shutdown(socket.SHUT_WR)

    rec_data = []
    while 1:
        data = s.recv(1024)
        if not data:
            break
        rec_data.append(data)

    s.close()
    return rec_data

if __name__ == '__main__':
    text_to_send = '=\xa0r\xfd#\x13\x06r\x0b-\xa6\xa1H\xb12=E\xb9\x07\x9f_\x04\xe3f\xcc\x02Fk04U\x9d\xef\xc0\x1ey\xd2\x0c\xbb\x12G\xceZ\xe8\rd\x10\x98s'
    text_recved = netcat( text_to_send)
    print text_recved[1]
