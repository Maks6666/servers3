import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 8081))

print("Connected to the server. You can start the game by sending a word.")

while True:
    word = input("Enter your word (or type 'stop' to quit): ")
    if not word:
        continue

    client.send(word.encode())

    if word == 'stop':
        print("You stopped the game.")
        break

    data = client.recv(1024).decode()
    if data == "Server stopped the game. You win!":
        print(data)
        break
    if data == "Wrong start letter. You lose!":
        print(data)
        break
    print("Server:", data)

client.close()
print("Disconnected from the server.")
