
from magic import getMagicNumber
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import sys

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
quit = 0
# Create server
with SimpleXMLRPCServer(('localhost', 8080),
                        requestHandler=RequestHandler,logRequests=False) as server:
    server.quit = 0
    server.register_introspection_functions()

    server.register_function(getMagicNumber, 'getMagicNumber')

    def kill():
        global quit
        quit = 1
        return 1
        
    server.register_function(kill, 'kill')

    # Run the server's main loop
    while not quit:
        server.handle_request()

   

