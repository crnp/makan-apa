import random

light = ['Sandwich', 'Burger']
general = ['Nasi Padang', 'Ayam', 'Steak']
all = light+general


def mauNggak(list):
    breakOutFlag = False
    while True:
        if breakOutFlag:
            break
        makanan = random.choice(list)
        print('\nMakan', makanan, 'mau?')
        print('1. Yuk!')
        print('2. Nggak ah')
        y = input('Jawab: ')
        while True:
            try:
                while int(y) not in (range(1, 3)):
                    raise ValueError

                match y:
                    case '1':
                        print('\nOke! Kita makan', makanan)
                        breakOutFlag = True
                        break
                    case '2':
                        print('\nKalo...')
                        break
                    case _:
                        raise ValueError
            except ValueError:
                y = input('\nMau nggak??\n')


def kasihSaranMakanan(x):
    match x:
        case '1':
            mauNggak(all)
        case '2':
            mauNggak(general)
        case '3':
            mauNggak(light)
        case '4':
            print('\nMakan bego lu belom makan juga\n')


print('Mau makan apa?')
print('1. Terserah')
print('2. Laper banget')
print('3. Laper dikit')
print('4. Gajadi deh')
x = input('Jawab: ')

while True:
    try:
        if int(x) not in range(1, 5):
            raise ValueError
        kasihSaranMakanan(x)
        break
    except ValueError:
        x = input('\nHah?\n')
