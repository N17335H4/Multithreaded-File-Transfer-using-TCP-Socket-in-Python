import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4456
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@")

        if cmd == "DISCONNECTED":
            print(f"[SERVER]: {msg}")
            break
        elif cmd == "OK":
            print(f"{msg}")

        data = input("> ")
        data = data.split(" ")
        cmd = data[0]

        if cmd == "HELP":
            client.send(cmd.encode(FORMAT))
        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))
            break
        elif cmd == "LIST":
            client.send(cmd.encode(FORMAT))
        elif cmd == "DELETE":
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))
        elif cmd == "UPLOAD":
            path = data[1]
            with open(f"{path}", "r") as f:
                bigfile = f.read()       
            smallfile = None
            lines_per_file = 300
            for lineno, line in enumerate(bigfile):
            	if lineno % lines_per_file == 0:
            		if smallfile:
            			smallfile.close()
            		small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
            		smallfile = open(small_filename, "w")
            	smallfile.write(line)
            	with open(small_filename, "r") as f:
            		text = f.read()
            	sfname = path.split("/")[-1]
            	send_data = f"{cmd}@{sfname}@{text}"
            	client.send(send_data.encode(FORMAT))

    print("Disconnected from the server.")
    client.close()

if __name__ == "__main__":
    main()
         	



    				
    			
    			
    			
    			