import socket
from _thread import *
import pickle
from player import Player
from game import Game, Turn

# this is the(a) server script, it always has to be running, need to first run this server
# script, and we can try to connect clients to it

server = "192.168.0.11"  # this is a local network, so on the same wifi
# to get the local ip address, type ipconfig to the command prompt
port = 5555  # this is a port that's typically open
# this is for an IPV4 address socket.AF_INET is the type we'll use and SOCK_STREAM is how the server string comes in
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# will do a try/catch statement here in case the server and port fail to bind to the socket
try:
    s.bind((server, port))  # bind the ip address (server) to this given port
except socket.error as e:
    str(e)

# the parameter is the number of clients to be able to connect to the server
s.listen(2)
print("Waiting for a connection, Server Started")

players = [Player("circle", True), Player("cross", False)]
game = Game("circle")

# defining a threaded function
def threaded_client(conn, player):
    if player % 2 == 0:
        symb = 'circle'
    else:
        symb = 'cross'
    conn.send(str.encode(symb))
    # want to send a message to confirm the connection

    reply = ""
    while True:
        try:
            # we're putting in 2048 bits, the amount of info we're receiving
            data = pickle.loads(conn.recv(2048))


            #players[game] = data
            # we need to decode the information received, as it is encoded over a client server system
            # utf-8 is the format'''
            # reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                # player.turn = False
                if game.valid_move(data):
                    game.add_move(data)
                    game.change_turn()
                    game.check_victory()
                if player == 1:
                    reply = game
                else:
                    reply = game
                # reply.turn = not reply.turn
                print("Received: ", data)
                print("Sending:", reply)
            # this is just encoding it into a bites object
            conn.sendall(pickle.dumps(reply))
        except:
            break

    #game = Game("circle")
    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    # s.accept() accepts any incoming connections and it will store the connection and the address
    conn, addr = s.accept()
    print("Connected to:", addr)
    # A thread is just another process that's running in the background
    # we don't want to end the previous threaded_client when we run another one
    # we want threaded_client to run in the background'''
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
