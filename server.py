import socket

# def connection():
#     address = input("Insert server ip")
#     port = 44444
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind((address, port))
#     s.listen(1) 
#     print("Server started! Waiting for connections...")
#     while True:
#         accept_connection(s)

# def accept_connection(s):
#     connection, address = s.accept()
#     print('Client connected with address:', address)
#     t=thread.Threading(target=message, args=(connection,))
#     t.start()

if __name__ == '__main__':
	port = 5687
	