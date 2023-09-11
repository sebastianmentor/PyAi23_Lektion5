int_to_str_map_numbers_0_to_10000 = {} 
str_to_int_map_numbers_0_to_10000 = {}  

for i in range(10001):
    int_to_str_map_numbers_0_to_10000[i] = f'{i}'
    str_to_int_map_numbers_0_to_10000[f'{i}'] = i


while True:
    value = input('Skriv en siffra >>> ')
    if value == 'q':
        break

    print(f'Först får vi in {value=} som {type(value)=}', end='\n\n')

    print(f'''Därefter kan vi avbilda strängar till int:
    {str_to_int_map_numbers_0_to_10000[value]=}
    {type(str_to_int_map_numbers_0_to_10000[value])=}'''
    , end='\n\n')

    integer = str_to_int_map_numbers_0_to_10000[value]
    print('Vi ansätter "integer = str_to_int_map_number_0_to_10000[value]"', end='\n\n')
    print(f'{integer=}, {type(integer)=}')

    print('Vi kan därefter gå tillbaka till string:')
    print(f'{int_to_str_map_numbers_0_to_10000[integer]=}', end='\n\n')