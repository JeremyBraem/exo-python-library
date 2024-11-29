from Application import Application
import socketserver
import json
import jsonpickle

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("Received from {}:".format(self.client_address[0]))
        method, params = self.data.decode('utf-8').split('//')
        application = Application()
        actions = {
            "display_books": application.display_books,
            "buy_book": application.buy_book,
            "add_book_in_bookshop": application.add_book_in_bookshop,
            "3": application.save_library,
            "4": application.reload_library,
            "5": application.exit_program,
        }
        action = actions.get(method)
        print(params)
        if action:
            response = action(params)  # Appel de la fonction associée
        else:
            response = "Veuillez sélectionner une option entre 1 et 5."
        print(jsonpickle.encode(response).encode('utf-8'))
        # just send back the same data, but upper-cased
        self.request.sendall( jsonpickle.encode(response).encode('utf-8') )

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()