invoernummer = int(input("Van welk getal wilt u de tafel zien? "))
def getallen(nummer: int):
    for getal in range(1,11):
        print(getal, " x ", nummer, " = ", getal * nummer)
getallen(invoernummer)