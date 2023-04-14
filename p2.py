import os
from time import sleep
while True:
    n = input('qual o seu nome?')
    i = int(input('qual a sua idade?'))
    print ('ola senhor(a)', n)
    print ('sua idade é:', i)
    if i > 0 and i < 13:
        print ('você é uma crianca')
    if i > 13 and i < 19:
        print ('você é jovem')
    if i > 19 and i < 60:
        print ('você é adulto')
    if i > 60 and i < 999:
        print ('você está velho')
    sleep(5)
    os.system('cls')

