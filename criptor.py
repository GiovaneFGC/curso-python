import hashlib
import random






senha = input ('insira sua senha:')
print ('sua senha é:', senha) 
r = random.randint(0,99999999999)
s = senha + str(r)
hash = hashlib.sha512( str( s ).encode("utf-8") ).hexdigest()
print ('sua senha criptografada é : ',hash)
