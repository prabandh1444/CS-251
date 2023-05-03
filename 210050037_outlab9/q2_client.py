import xmlrpc.client
import sys
s = xmlrpc.client.ServerProxy('http://localhost:8080')

num = sys.argv[1]

print(s.getMagicNumber(int(num)))

s.kill()

