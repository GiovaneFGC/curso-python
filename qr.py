import qrcode
while True:

    frase = input ('digite uma frase:')
    print (frase)
    if frase == 'sair':
        quit()
    img = qrcode.make(frase)
    img.save("some_file.png")