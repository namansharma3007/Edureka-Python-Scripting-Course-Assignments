import re
from cryptography.fernet import Fernet

print("Please enter an ID having one uppercase letter, one lowecase letter, atleast one digit from 0-9 and one of the following symbols - $#@")
referenceId = input("Enter reference id:\n")

key = Fernet.generate_key()
fernet = Fernet(key)

def checkValidity(id):
    while(True):
        if len(id) > 12:
            break
        elif not re.search('[0-9]',id):
            break
        elif not re.search('[a-z]',id):
            break
        elif not re.search('[A-Z]',id):
            break
        elif not re.search("[$#@]",id):
            break
        else:
            return True
    return False


def encriptId(id):
    return fernet.encrypt(id.encode())


def decriptId(encId):
    return fernet.decrypt(encId).decode()

validity = checkValidity(referenceId)

if(validity):
    encriptedMessage = encriptId(referenceId)
    print("Encrypted ID:",encriptedMessage,"\n")
    print("Do you wish to get it decripted:")

    wish = input("Enter Y for yes and N for no:\n")

    if(wish.lower() == "y"):
        decMessage = decriptId(encriptedMessage)
        print("\nDecrypted ID:",decMessage)
    else:
        print("Thank You! Please visit us again")
else:
    print("Please enter a valid password")




