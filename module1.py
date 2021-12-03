def adding():
    #Программа добавляет в списки имя и зарплату
    #esimene arv nimi: str
    #teine arv - palk: int 
    #rtype var: str
	nimi=input("Введите имя: ")
	palk=input("Введите зарплату: ")
	with open("inimesed.txt", "a") as inimesed:
		inimesed.write(nimi+"\n")	
	with open("palgad.txt", "a") as palgad:
		palgad.write(palk+"\n")
def maks():
     #Программа проверяет списки и выводит на экран человека с максимальной зарплатой
    #rtype var: int
	palgad=[]
	with open("palgad.txt", "r") as f1:
		for stro in f1:
			palgad.append(stro.strip())
	f=open("inimesed.txt", "r")
	inimesed=[]
	for stroka in f:
		inimesed.append(stroka.strip())
	f.close
	zp=palgad.copy()
	zp.sort()
	a=zp[0]
	b=palgad.index(a)
	print("Самая большая зарплата у "+inimesed[b])
def min():
    #Программа проверяет списки и выводит на экран человека с самой маленькой зарплатой
    #rtype var: int
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
	"""
	"""
	palgad,inimesed=lists()
	summa=0
	for palk in palgad:
		summa+=float(palk)
	kesk=summa/len(palgad)
	print("keskmine palk "+kesk)
	vahe=0
	if kesk in palgad:
		kesk=inimesed[palgad.index(kesk)]
		print(kesk)
	else:
		kesk="puudub"
		print(kesk)