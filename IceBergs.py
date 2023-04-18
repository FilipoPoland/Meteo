# Pacyfik
# PR = (Vw * (Tz - Tp))/((1 + 0.4) * (Tw-Tz)
# Atlantyk
# PR = (Vw * (Tz - Tp))/((1 + 0.3) * (Tw-Tz)
# Tz = -0.0539 * S
# Vw = 1m/s = 2kn
# Tz - Temperatura zamarzania
# Tp - Temperatura powietrza
# Tw - Temperatura wody
# Vw - Predkosc statku

rP = input('Jeżeli prędkość jest w węzłach wpisz "t": ')
if rP == 't':
    Vw = float(input('Podaj predkość statku: '))
    Vw /= 2
else:
    Vw = float(input('Podaj predkość statku w m/s: '))

tmp = input('Jeżeli znane jest zasolenie wpisz "t" ')
if tmp == 't':
    S = float(input('Podaj zasolenie: '))
    Tz = -0.0539 * S
else:
    Tz = float(input('Podaj Temperaturę zamarzania: '))

Tp = float(input('Podaj temperaturę powietrza: '))
Tw = float(input('Podaj temperaturę wody: '))

rAkwen = input('Wybierz akwen - Pacyfik(p)/Atlantyk(a): ')
# Pacyfik

if rAkwen == 'p':
    print((Vw * (Tz - Tp))/((1 + 0.4) * (Tw-Tz)))

# Atlantyk

elif rAkwen == 'a':
    print((Vw * (Tz - Tp)) / ((1 + 0.3) * (Tw - Tz)))
