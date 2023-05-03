from http import client
import os
import sys
from urllib import response
host = sys.argv[1]
client = os.system("ping -c1 -w5 "+host+" > /dev/null 2>&1")
if client == 0:
    print('YES')
else:
    print('NO')