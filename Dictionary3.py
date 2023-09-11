account =  {}


while True:
    print('1. lägg till konto')
    print('2. avsluta')
    val = input('Val: ')
    if val == '1':
        account_number = input('Skriv kontonummer XXXXXX: ')

        if account_number in account:
            print('Kontonummeret finns redan')
        else:
            account[account_number] = 0

    elif val == '2':
        break
    else:
        print('Fel')

print(account)