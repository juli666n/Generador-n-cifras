n = int(input("ingrese cantidad de cifras\n"))
cont = 0
while len(str(cont)) <= n:
    contprint = str(cont)
    contprint = contprint.zfill(n)
    print (contprint)
    cont += 1
