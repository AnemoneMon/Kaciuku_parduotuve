kaciukai = [
    ['Meino meskenas','juoda', 6, 200],
    ['Sfinksas','smelio', 5, 300],
    ['Britu trumpaplaukis','pilka', 7, 350],
    ['Burmos','ruda/smelio', 4, 300],
    ['Bombejaus','juoda', 5, 400],
    ['Misrunas', 'raina', 2, 100]
]

def pradinis():
    print('1. Rodyti visas turimas kates')
    print('2. Ivesti nauja kate')
    print('3. Pakeisti turimos kates duomenis')
    print('4. Pasalinti turimos kates duomenis')
    print('5. Filtravimas')
    print('6. Iseiti is programos')

def rodytikate(kat, nr = 1):
    print(f'{nr}. Kates veisle - {kat[0]}, kailio spalva - {kat[1]}, amzius - {kat[2]} menesiai, kaina - {kat[3]} eurai')

def rodytivisas():
    nr = 1
    for kat in kaciukai:
        rodytikate(kat, nr)
        nr += 1
    print('************')

def pridetikate():
    print('Irasykite kates veisle:')
    veisle = input()
    print('Irasykite kates kailio spalva:')
    spalva = input()
    print('Irasykite kates amziu (menesiais):')
    amzius = int(input())
    print('Irasykite kates kaina:')
    kaina = int(input())
    kaciukai.append([veisle, spalva, amzius, kaina])

def pakeistikate():
    print('Iveskite kates iraso numeri, kuri norite pakeisti')
    nr2 = int(input())
    rodytikate(kaciukai[nr2 - 1])
    print('Irasykite kates veisle:')
    veisle2 = input()
    print('Irasykite kates kailio spalva:')
    spalva2 = input()
    print('Irasykite kates amziu (menesiais):')
    amzius2 = int(input())
    print('Irasykite kates kaina:')
    kaina2 = int(input())
    kaciukai[nr2 - 1] = [veisle2, spalva2, amzius2, kaina2]

def istrintikate():
    print('Iveskite kates iraso numeri, kuri norite istrinti')
    nr3 = int(input())
    kaciukai.pop(nr3 -1)

def filtravimas():
    print('Pasirinkite filtro tipa:')
    print('spalva')
    print('kaina')
    filtr = input()
    if filtr == 'spalva':
        print('Iveskite spalva:')
        spal = input()
        spalvos = []
        color_found = False
        for kate in kaciukai:
            if spal in kate:
                spalvos.append(kate)
                color_found = True
        if not color_found:
            print('Sios spalvos kates neturime')
        else:
            nr = 1
            for kat in spalvos:
                rodytikate(kat, nr)
                nr += 1
        print('************')

    if filtr == 'kaina':
        print('Iveskite norima kaina (bus rodoma +-50 euru):')
        kain = int(input())
        kainos = []
        price_found = False
        for kate in kaciukai:
            if kate[3] - 50 <= kain <= kate[3] + 50:
                kainos.append(kate)
                price_found = True
        if not price_found:
            print('Uz tokia kaina kates neturime')
        else:
            nr = 1
            for kat in kainos:
                rodytikate(kat, nr)
                nr += 1
        print('************')

print('*** Kaciuku parduotuves sistema ***')
print('Funkciju pasirinkimai:')

while True:
    pradinis()
    print('Irasykite funkcijos numeri, kuri norite atlikti:')
    pasirink = int(input())
    match pasirink:
        case 1:
            rodytivisas()
        case 2:
            pridetikate()
            rodytivisas()
        case 3:
            pakeistikate()
            rodytivisas()
        case 4:
            istrintikate()
            rodytivisas()
        case 5:
            filtravimas()
        case 6:
            exit(1)
