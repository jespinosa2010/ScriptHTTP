# Script para crear un fichero .htaccess

import sys
import hashlib

password = sys.argv[4]
passwordCifrado = password.encode('utf-8')
md5 = hashlib.md5(passwordCifrado).hexdigest()
print(md5)

if len(sys.argv) != 6:
    print("El programa necesita 6 argumentos.")
    sys.exit(1)
else:

    file = open(sys.argv[1] + "\.htpasswd","w")
    file.write(f"{sys.argv[3]}:{md5}")

    #print(sys.argv[0])
    file = open(sys.argv[1]+'\.htaccess','w')
    file.write("DirectoryIndex "+sys.argv[2]+'\n')
    file.write("AuthName \"Dialog prompt\"\n")
    file.write("AuthType Basic\n")
    file.write(sys.argv[1] + "\.htpasswd\n")
    #Options -Indexes
    if sys.argv[5] == 'S':
        file.write("Options -Indexes\n")



    
