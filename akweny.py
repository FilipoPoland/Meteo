import tkinter as tk

# pytanie o ilosc koniecnych podejsc
akwen = input('Ile jest akwenów?')
akwen = akwen.replace(' ', '')
akweny = akwen

# oddanie ilosci akwenow
print('Ilość akwenów to:', akweny)

# lista gestosci
listg = list()

for h in range(int(akweny)):

    # dwa pytania wstepne dla uzytkownika
    S = input('Jakie jest zasolenie wody?\n')
    S = S.replace(',', '.')
    S = S.replace(' ', '')
    Tw = input('Jaka jest temperatura wody?\n')
    Tw = Tw.replace(',', '.')
    Tw = Tw.replace(' ', '')

    # gestosc umowna
    Pu = (28.1522 - (0.0735 * float(Tw)) - (0.00469 * (float(Tw) ** 2)) + (0.802 - (0.002 * float(Tw))) *
          (float(S) - 35.0))

    # rownanie dla gestosci
    g = float(Pu) / 1000 + 1

    # add to list
    listg.append(g)

    # usuniecie z wartosci akwenow pozostalych jednego z nich
    akweny = int(akweny) - 1
    print("pozostałe akweny:", akweny)

    # pomocnicza linia opisuje pozniejsza wartosc r
    print('Gęstość wody:', g)

# check for the list
print('Zasolenie:', listg)

# wiadomosci wstepne
zanurzenie0 = input('Jakie jest wyjściowe zanurzenie statku?')
Leftakweny = (int(akwen) - 1)
n = 0
zanurzenie = 0

# lista zanurzenia
listz = list()

for h in range(Leftakweny):

    # zdefiniowanie zasolen
    gestosc1 = n
    gestosc2 = 1 + n

    # obliczenie zanurzenia
    zanurzenie = ((float(listg[int(gestosc1)]))/float(listg[int(gestosc2)])) * float(zanurzenie0)

    # dodanie do listy zanurzenia
    listz.append(zanurzenie)

    # redefiniowanie zanurzenia0
    zanurzenie0 = zanurzenie

    # redefiniowanie n
    n = n + 1

print('Zanurzenia:', listz)
input('Naciśnij enter, aby zkończyć.')
