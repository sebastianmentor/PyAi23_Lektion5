barcelona =  {}

barcelona[9]= 'Lewan'
barcelona[8]= 'Pedri'
barcelona[44]= 'Carlsson'
barcelona[32]= 'Reza'

pythonutvecklarna = {1:'Sebastian',
                     2:'Emanuel',
                     3:'Daniel',
                     4:'Jens',
                     9:'Mannpret'
}


# print(barcelona)
# print(pythonutvecklarna)

# for key, value in barcelona.items():
#     print(f"Spelare {value} har tröjnummer {key}")

# for player in barcelona.values():
#     print(player)

barcelona.update(pythonutvecklarna)
print(barcelona) 