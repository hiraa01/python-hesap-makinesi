#hesap makinesi yapıp kullanıcıdan alınan 2 sayıya aşağıdaki işlemleri yaptır.
#toplama
#çıkarma
#çarpma
#bölme
#mod alma
#integer division tam sayı bölmesi
#üs alma
#her iki sayının karekökü
import math
while True: 
    x=int(input("birinci sayıyı giriniz: "))
    y=int(input("ikinci sayıyı giriniz: "))
    a=input("yapmak istediğiniz işlem nedir?(+,-,*,/,%,//,**,sqrt bu işlemlerden birini giriniz.) ")
    if a=='+':
        print("{} + {} = {}".format(x,y, x+y))
    elif a=='-':
        print("{} - {} = {}".format(x,y, x-y))
    elif a=='*':
        print("{} * {} = {}".format(x,y, x*y))
    elif a=='/':
        print("{} / {} = {}".format(x,y, x/y))
    elif a=='%':
        print("{} % {} = {}".format(x,y, x%y))
    elif a=='//':
        print("{} // {} = {}".format(x,y, x//y))
    elif a=='**':
        print("{} ** {} = {}".format(x,y, x**y))
    elif a=='sqrt':
        print("{} , {} = {} , {}".format(x,y, math.sqrt(x), math.sqrt(y)))