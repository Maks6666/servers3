# Реалізуйте клієнт-серверний додаток, що дозволяє двом
# користувачам грати в гру «Слова». Один із
# гравців ініціює гру. Якщо другий гравець підтверджує, то
# гра починається. Гру можна припинити. Той хто припинив
# гру — програв. Після завершення гри можна ініціювати повторний матч.

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 8081))
server.listen(1)

print("Waiting for a player...")

client, address = server.accept()
print(f"Connection from {address}")

last_letter = None

while True:
    data = client.recv(1024).decode()
    print("Player:", data)

    if data == 'stop':
        print("Player stopped the game.")
        break


    if last_letter:
        print("Word does not start with the correct letter.")
        client.send("Wrong start letter. You lose!".encode())
        break


    response = input("Enter your word: ")

    if response == 'stop':
        print("Server stopped the game.")
        client.send("Server stopped the game. You win!".encode())
        break


    last_letter = response[-1]

    client.send(response.encode())

client.close()
server.close()
print("Game over.")








