import socket
import sys
import http.client
import urllib.parse
import board


def send_message(ip, port, x, y, local):
    params = urllib.parse.urlencode({"x": x, "y": y})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    #If not locally hosting
    if local == 0:
        conn = http.client.HTTPConnection(ip, port)
    elif local == 1:
        conn = http.client.HTTPConnection(socket.gethostbyname('localhost'), 1040)
    else:
        print("No Connection Made")

    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    data = response.reason
    print(data)
    print(response.status)

    if 'sink' in data:
        data = data.replace("hit=", "")
        data = data.replace("sink=", "")
        data = data.split('&')
        print('Sunk %s' % data[1])
        board.process_request(x,y, 'opponent_board.txt', 'X')
    elif 'hit' in data:
        print(data)
        data = int(data.replace("hit=", ""))
        if data == 0:
            board.process_request(x, y, 'opponent_board.txt', 'O')
        elif data == 1:
            board.process_request(x, y, 'opponent_board.txt', 'X')
    conn.close()


if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
    x = int(sys.argv[3])
    y = int(sys.argv[4])
    local = int(sys.argv[5])

    send_message(ip, port, x, y, local)