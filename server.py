import socket
import json

def handle_request(data):
    request = json.loads(data)
    method = request["method"]
    params = request["params"]
    id = request["id"]
    
    result = None
    if method == "subtract":
        result = params[0] - params[1]

    response = {
        "results": str(result),
        "result_type": "int",
        "id": id
    }
    return json.dumps(response)

def main():
  #TCP/IP ソケットを使用
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # ローカルホストのポート6000で待ち受け
    sock.bind(('localhost', 6000))
    sock.listen(1)
    print("Listening on port 6000...")
    
    while True:
        connection, client_address = sock.accept()
        try:
            data = connection.recv(1024)
            if data:
                response = handle_request(data.decode('utf-8'))
                connection.sendall(response.encode('utf-8'))
        finally:
            connection.close()

if __name__ == "__main__":
    main()
