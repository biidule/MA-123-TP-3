# -*- coding: utf-8 -*-
"""
fait le Mon Mar  1 10:06:10 2021

par thibault pelliccia
"""
import math as m

def g(f,fp,x):
    return x-f(x)/fp(x)
############################### f1 x**4+3x=9

def f1(x):
    return x**4 + 3*x - 9
def f1p(x):
    return 4*(x**3)+3

############################### f2 x=3cosx-2

def f2(x):
    return 3*m.cos(x)-2-x
def f2p(x):
    return -3*m.sin(x)-1

################################### f3 xe^x=7

def f3(x):
    return x*m.exp(x)-7
def f3p(x):
    return x*m.exp(x)+m.exp(x)
################################### f4 

def f4(x):
    return m.exp(x)-x-10
def f4p(x):
    return m.exp(x)-1
###################################

def f5(x):
    return 2*m.tan(x)-x-5
def f5p(x):
    return (2/m.cos(x)**2)-1
###################################

def f6(x):
    return m.exp(x)-(x**2)-3
def f6p(x):
    return m.exp(x)-2*x
###################################

def f7(x):
    return 3*x+4*m.log(x)-7
def f7p(x):
    return 3+(4/x)
###################################

def f8(x):
    return x**4-2*(x**2)+4*x-17
def f8p(x):
    return 4*(x**3)-4*x+4
###################################

def f9(x):
    return m.exp(x)-2*m.sin(x)-7
def f9p(x):
    return m.exp(x)-2*m.cos(x)
###################################
def g10(x):
    return 0
def f10(x):
    return m.log(x**2+4)*m.exp(x)-10
def f10p(x):
    return ((2*x))/((x**2)+4)*m.exp(x)+m.log(x**2+4)*m.exp(x)

def newton(f,fp,x0,epsilon,Nitermax) :
    n=0
    xold=x0
    xnew=g(f,fp,xold)
    erreur=(xnew-xold)
   
    while ( abs(erreur) > epsilon) and n<Nitermax:
        xnew=g(f,fp,xold)
        erreur=xnew-xold
        xold=xnew
        print(xnew,erreur,n)
        n+=1


newton(f10,f10p,2, 1e-10, 1e4)   #g, x0, epsilon, nitermax