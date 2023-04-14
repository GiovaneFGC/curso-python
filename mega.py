import random
while True:
    a = int(input(' quantos jogos?'))
    if a == 0:
        quit()
    for a in range (1,a+1):
        print ('jogo', a, ":")
        num = " "
        for b in range (1,16):
            r = random.randint(1900,2001)
            num = num+" "+str(r)
        print (num) 