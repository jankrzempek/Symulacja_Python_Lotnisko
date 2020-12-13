import random
import arrow

# liczba osoób stała i od niej wyliczamy 10% osoób VIP

#Liczba kolejek jest liczbą zmienną z zakresu [1,5]

#możemy wyszczególnić dwa tempa osób działających na kasie czyli tempo tz - jest to stała oraz tu jest to zmienna z zakresu [0.15,0.30]

#dla kazxdej z osób będziemy losowac jego wagę bagażu

#odstęp pomiędzy dwoma klientami wynosi 10 sek

# PROGRAM ZWRACA : tempo osbługi średnie jednej osoby zwykłej oraz VIP, łączny czas osbługi wszystkich klientów.


def ileJestOsob():
    liczbaWylosowana = random.randint(50,100)
    liczbaOsobVIP = int(0.1 * liczbaWylosowana)
    liczbaKas = random.randint(1,5)
    return (liczbaWylosowana,liczbaOsobVIP,liczbaKas)

def mieszajOsoby(liczbaWylosowana):
    array = []
    for index in range(1,liczbaWylosowana+1):
        array.append(index)
    random.shuffle(array)
    return array

def wylosowanieWagiWalizki():
    waga = random.randint(1,150)
    return waga

def tempo():
    tempoUczacego = random.uniform(0.15,0.30)
    return tempoUczacego

def losujPracownikow(liczba):
    tablicaTemp = []
    tempoStalego = 0.1
    iloscPracownikowUczacych = random.randint(1,liczba-1)
    iloscPracownikowStalych = liczba - iloscPracownikowUczacych
    for index in range(iloscPracownikowUczacych):
        tablicaTemp.append(round(tempo(),3))
    for index in range(iloscPracownikowStalych):
        tablicaTemp.append(tempoStalego)
    return tablicaTemp
def procesPrzyporzadkowania(liczbaKas,zbiorOsob,liczbaVIP):
    dlugaKolejka = []
    listaCzasow = []
    listaWag = []
    for index in range(len(zbiorOsob)):
        # 100 to wartość stała sekund jako podstawa u każdej z osób
        #czasObsługiKlienta = int(wylosowanieWagiWalizki() * tempo())
        czasObslugiKlienta = 0.1
        lacznaWaga = int(wylosowanieWagiWalizki())
        if zbiorOsob[index] <= liczbaVIP:
            dlugaKolejka.insert(0,zbiorOsob[index])
            listaCzasow.insert(0,czasObslugiKlienta)
            listaWag.insert(0, lacznaWaga)
        else:
            dlugaKolejka.append(zbiorOsob[index])
            listaCzasow.append(czasObslugiKlienta)
            listaWag.append(lacznaWaga)
    tablicaOdwzorujacaKasy = []
    tablicaCzasowDoKolejnychKolejek = [0,0,0,0,0]
    tablicaWagDoKolejnychKolejek = [0, 0, 0, 0, 0]
    #otwarcie kas
    for liczba in range(liczbaKas):
      tablicaOdwzorujacaKasy.append(1)
    print("************************")
    print("Lista czasów obsługi")
    print(listaCzasow)
    print("************************")
    print("Lista kolejności ustwawienia w kolejce")
    print(dlugaKolejka)
# TODO : działamy na pręsdkości kas
    tablicaTempPracownikow = losujPracownikow(liczbaKas)

    print("************************")
    print(tablicaTempPracownikow)

    zmienna = 0
    koniecOblslugi0 = 0
    koniecOblslugi1 = 0
    koniecOblslugi2 = 0
    koniecOblslugi3 = 0
    koniecOblslugi4 = 0

    starCalosci = arrow.now()
    while zmienna != len(dlugaKolejka)-1:

        if tablicaOdwzorujacaKasy[0] == 1:
            obslugujeKlienta = listaWag[zmienna] * tablicaTempPracownikow[0]
            tablicaCzasowDoKolejnychKolejek[0] += obslugujeKlienta
            tablicaWagDoKolejnychKolejek[0] += listaWag[zmienna]
            start = arrow.now()
            tablicaOdwzorujacaKasy[0] = 0
            koniecOblslugi0 = start.shift(seconds=obslugujeKlienta)
            zmienna += 1
        if arrow.now() >= koniecOblslugi0:
            tablicaOdwzorujacaKasy[0] = 1
        if liczbaKas > 1:
            if tablicaOdwzorujacaKasy[1] == 1:
                obslugujeKlienta = listaWag[zmienna] * tablicaTempPracownikow[1]
                tablicaCzasowDoKolejnychKolejek[1] += obslugujeKlienta
                tablicaWagDoKolejnychKolejek[1] += listaWag[zmienna]
                start = arrow.now()
                tablicaOdwzorujacaKasy[1] = 0
                koniecOblslugi1 = start.shift(seconds=obslugujeKlienta)
                zmienna += 1
            if arrow.now() >= koniecOblslugi1:
                tablicaOdwzorujacaKasy[1] = 1
            if liczbaKas > 2:
                if tablicaOdwzorujacaKasy[2] == 1:
                    obslugujeKlienta = listaWag[zmienna] * tablicaTempPracownikow[2]
                    tablicaCzasowDoKolejnychKolejek[2] += obslugujeKlienta
                    tablicaWagDoKolejnychKolejek[2] += listaWag[zmienna]
                    start = arrow.now()
                    tablicaOdwzorujacaKasy[2] = 0
                    koniecOblslugi2 = start.shift(seconds=obslugujeKlienta)
                    zmienna += 1
                if arrow.now() >= koniecOblslugi2:
                    tablicaOdwzorujacaKasy[2] = 1
                if liczbaKas > 3:
                    if tablicaOdwzorujacaKasy[3] == 1:
                        obslugujeKlienta = listaWag[zmienna] * tablicaTempPracownikow[3]
                        tablicaCzasowDoKolejnychKolejek[3] += obslugujeKlienta
                        tablicaWagDoKolejnychKolejek[3] += listaWag[zmienna]
                        start = arrow.now()
                        tablicaOdwzorujacaKasy[3] = 0
                        koniecOblslugi3 = start.shift(seconds=obslugujeKlienta)
                        zmienna += 1
                    if arrow.now() >= koniecOblslugi3:
                        tablicaOdwzorujacaKasy[3] = 1
                    if liczbaKas > 4:
                        if tablicaOdwzorujacaKasy[4] == 1:
                            obslugujeKlienta = listaWag[zmienna] * tablicaTempPracownikow[4]
                            tablicaCzasowDoKolejnychKolejek[4] += obslugujeKlienta
                            tablicaWagDoKolejnychKolejek[4] += listaWag[zmienna]
                            start = arrow.now()
                            tablicaOdwzorujacaKasy[4] = 0
                            koniecOblslugi4 = start.shift(seconds=obslugujeKlienta)
                            zmienna += 1
                        if arrow.now() >= koniecOblslugi4:
                            tablicaOdwzorujacaKasy[4] = 1

    koniecCalosci = arrow.now()
    czasObslugiKolejki = koniecCalosci - starCalosci
    print("************************")
    print("Calkowity Czas Obslugi Kolejki")
    print(czasObslugiKolejki)
    print("************************")
    print("Czas obsługi kolejek 1|2|3|4|5")
    for i in range(liczbaKas):
        print(f"{round(tablicaCzasowDoKolejnychKolejek[i],2)} sek| ", end= "")
    print("")
    print("************************")
    print("Wagi łączne dla kolejek 1|2|3|4|5")
    for i in range(liczbaKas):
        print(f"{tablicaWagDoKolejnychKolejek[i]} kg| ", end="")



# Tutaj się będzie wszystko wydarzać
if __name__== '__main__':
    liczbaWylosowanych,liczbaOsobVIP,liczbaKas = ileJestOsob()
    print("************************")
    print("Liczba kas")
    print(liczbaKas)
    print("************************")
    print("Liczba osob VIP")
    print(liczbaOsobVIP)
    print("************************")
    print("Liczba osob zwykłych")
    print(liczbaWylosowanych)
    print("************************")
    zbiorOsobWylosowanych = mieszajOsoby(liczbaWylosowanych)
    procesPrzyporzadkowania(liczbaKas,zbiorOsobWylosowanych,liczbaOsobVIP)