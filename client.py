import socket

def main(): 

	host = "127.0.0.1"
	port = 8080

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((host, port))
		data = b"hello world"
		s.sendall(data)
		rec = s.recv(1024)
		print(rec)
		command = rec.decode("utf-8").split(":")[0]
		print(command)
		if command == "en":
			encryptData("file")

def encryptData(fileName):
	return

if __name__ == "__main__":
	main()
