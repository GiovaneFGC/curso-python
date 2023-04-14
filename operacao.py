import math
from decimal import Decimal  

def somar (x,y):
    resultado = x + y
    return resultado
def subtrair (x,y):
    resultado = x - y
    return resultado
def multiplicar (x,y):
    resultado = x * y
    return resultado    
def dividir (x,y):
    resultado = x / b 
    return resultado
def exponencial (x,y):
    resultado = x ** y
    return resultado
def calcular (x,y):
    a = x**2
    b = x**y
    c = (a+b)**y
    d = x+1
    e = (y/d)+1 
    resultado = Decimal(c)/Decimal(e)
    return resultado

a = int (input("digite A:"))
b = int (input("digite B:"))
print ("a+b = ", somar(a,b))
print ("a-b = ", subtrair(a,b))
print ("a*b = ", multiplicar(a,b))
print ("a/b = ", dividir(a,b))
print ("a**b =", exponencial(a,b))
print ("calcular=", calcular(a,b))




