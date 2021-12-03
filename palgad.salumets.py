from module1 import*
palk=[1200,2500,750,395,1200]
inimesed=["Mark","Albert","Nikita","Denis","Vadim"]
def palgad(p,i):
    valik=input("Средняя зарплата - 1,\nМинимальная зарплата - 2,\nМаксимальная зарплата - 3,\nУдалить человека - 4,\")
    if valik=="1":
        kesk_palk=round(keskmine(palk),2)
        print("Keskmine palk on ",kesk_palk)
        print()
        print()
    elif valik=="2":
        m_palgad,nimi=minimum(palk,inimesed)
        for n in nimi:
            print(m_palgad[0], " будет получено ",n)
            print()
            print()
    elif valik=="3":
        max_palk,kto=maksimum(palk,inimesed)
        print("Максимальная зарплата ", max_palk, " будет получено ",kto)
        print()
        print()
    elif valik=="4":                                       
        p,i=delete(palk,inimesed)
        print(palk,inimesed)
        if len(inimesed)==0:
            print("Tühi list")
while True:
    palgad(palk,inimesed)
        
        
