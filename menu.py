import requests

def incluir():
    a=(input("Informe o seu CPF:"))
    b=(input("Informe o seu nome:"))
    c=(input("Informe o seu telefone:"))
    d=(input("Informe o seu email:"))
    return "incluido com sucesso"
    
def excluir():
    cpf = (input("qual o id a ser excluido?:"))

    x = chamar_api("delete", cpf, "excluir/")
    return "excluido com sucesso"

def excluirid():
    id = (input("qual o id a ser excluido?:"))

    x = chamar_api("delete", id, "excluirid/")
    return "excluido com sucesso"

def listar():
    return "listar"

def chamar_api (verbo: str, dados:str, ms:str):
    r=None
    URL = ("http://127.0.0.1:8000/")
    if verbo == "delete"
        x = URL + ms + dados
        print ("teste " + x)
        r = requests.delete (x, json = dados)
    if verbo == "get":
        return r.text   

def exibe():    
    print ("                                [][][][][][][][][][][][] menu [][][][][][][][][][][][][][]")
    print (" ")
    print ("                                                     1 - incluir")
    print ("                                                     2 - excluir")
    print ("                                                     3 - listar")
    print ("                                                     4 - excluir id")
    print ("                                                     0 - sair")
    print (" ")
    opt=int(input("Escolha uma opção:"))
    return opt
if __name__ == "__main__":
    while True:
        x = exibe()
        if x == 0:
            exit()
        if x == 1:
            print(incluir())
        if x == 2:
            print(excluir())
        if x == 3:
            print(listar())
        if x == 4:
            print(excluirid())
    
