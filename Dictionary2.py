# pris_lista = dict(oljefilter = 129.9,
#                   torkarblad = 59.0,
#                   luftfilter = 299.0,
#                   skivbromsar = 999.9,
#                   däck_styck = 500,
#                   däck_packet_4_st = 1500)

pris_lista = {  1: 129.9,
                2: 59.0,
                3: 299.0,
                4: 999.9,
                5: 500,
                6: 1500}


while True:
    print('1. Lägg till produkt!')
    print('2. Avsluta')
    val = input('Gör ett val: ')
    if val == '1':
        köp = 0
        while True:
            for key in pris_lista:
                print(f"Skriv in '{key}' om du önskar lägga till detta i ditt köp!")
            vara_eller_avsluta = input('\nSkriv in önskad produkt eller Q för att avsluta\n>>>')

            if vara_eller_avsluta.lower() == 'q':
                break
            elif vara_eller_avsluta in pris_lista:    
                antal = int(input("\nSkriv in antal!"))
                köp += antal*pris_lista[vara_eller_avsluta]
            else:
                print('Fel val!!!!')
        print('Kostnaden blev', köp)

    elif val == '2':
        break
    else:
        print('Gör korrekt val!')
