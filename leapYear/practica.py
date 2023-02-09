def anoBisiesto(year):
    if year %4 == 0:
        if year %100 == 0:
            if year %400 == 0:
                print("AÑO BISIESTO")
            else:
                print("EL AÑO NO ES BISIESTO")
        else:
            print("AÑO BISIESTO")
    else:
        print("EL AÑO NO ES BISIESTO")

anoBisiesto(1900)