#My_cualc
from secrets import choice
from webbrowser import get


def getNum():
    fNum=float(input("plz eneter first number"))
    sNum=float(input("plz enter secound number"))
    return fNum,sNum
    
def add():
    x,y=getNum()
    return x+y
def mul():
    x,y=getNum()
    return x*y
def div():
    x,y=getNum()
    return x/y
def dif():
    x,y=getNum()
    return x-y
def mod():
    x,y =getNum()
    return x%y

print(''' 
1.add
2.mul 
3.div
4.dif
5.mod
''')
choice=choice-1
chioce=int(input("enter your choice :"))
operatoins=[add,mul,div,dif,mod]
choice-1
output=operatoins[choice]()
print(output)
