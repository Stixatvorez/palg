def adding():
 """Добавление человека и зп
 """
	nimi=input("Введите имя: ")
	palk=input("Введите зарплату: ")
	with open("inimesed.txt", "a") as inimesed:#добовляем человека
		inimesed.write(nimi+"\n")	
	with open("palgad.txt", "a") as palgad:#добовляем зп
		palgad.write(palk+"\n")
def maks():
"""вычисление самой большой зп
"""
	palgad=[]
	with open("palgad.txt", "r") as f1:#открываем файл зп
		for stro in f1:
			palgad.append(stro.strip())
	f=open("inimesed.txt", "r")
	inimesed=[]
	for stroka in f:
		inimesed.append(stroka.strip())
	f.close#закрываем файл
	zp=palgad.copy()
	zp.sort()
	a=zp[0]
	b=palgad.index(a)
	print("Самая большая зарплата у "+inimesed[b])
def min():
"""вычисление мин зп
"""
	palgad=[]
	with open("palgad.txt", "r") as f1:
		for strok in f1:
			palgad.append(strok.strip())
	inimesed=[]
	f=open("inimesed.txt", "r")
	inimesed=[]
	for stroka in f:
		inimesed.append(stroka.strip())
	zp=palgad.copy()
	zp.sort()
	zp.reverse()
	a=zp[0]
	b=palgad.index(a)
	print("Самая маленькая зарплата у "+inimesed[b])
def keskmine():
    """проверяет списки и выводит на экран среднюю зарплату
    """
    sum=0
    for palgad in p:
        sum+=palk
    keskm=sum/len(palgad)
    print(keskm)
    v=0
    if 0<p.index(keskm)<len(p)-1:
        kesk=i(p.index(keskm))
        return keskm
    else:
        print("Нет средней зарплаты")
        return keskm
