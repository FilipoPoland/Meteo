import tkinter
from tkinter import Label


def density(water_temp, salinity):
    pu = (28.1522 - (0.0735 * float(water_temp)) - (0.00469 * (float(water_temp) ** 2)) +
          (0.802 - (0.002 * float(water_temp))) * (float(salinity) - 35.0))
    g = float(pu) / 1000 + 1
    return g


def draughts(densty_list, zanurzenie0):
    global l_znrz
    try:
        l_znrz.append(float(pol_usr(zanurzenie0)))
    except:
        print('Podano złą wartość zanurzenia początkowego.')
    print(f'Count: {count}')
    for i in range(count - 2):
        zanurzenie = ((float(densty_list[i])) / float(densty_list[(i + 1)])) * float(zanurzenie0)
        l_znrz.append(zanurzenie)
        zanurzenie0 = zanurzenie
    return l_znrz


def pol_usr(get_input):
    fr_cptr = get_input.replace(',', '.')
    fr_cptr = fr_cptr.replace(' ', '')
    return fr_cptr


def btnpress():
    counting()

    # to mimo dodawania pól nie robi dla mnie nic przydatnego bo nie wiem jak odwołać się do tych pół
    # akwen nazwa
    lbl = tkinter.Label(text=f'Akwen {count - 1}')

    # pola
    key = f'num{count - 1}'
    d_tw[key] = tkinter.Entry(root, validate='key')
    d_zsl[key] = tkinter.Entry(root, )

    # akwen nazwa
    lbl.grid(column=1, row=count)
    # temperatura wody
    d_tw[key].grid(column=2, row=count)
    # zasolenie
    d_zsl[key].grid(column=3, row=count)


def counting():
    global count
    count += 1
    return count


def btncalc():
    global tw_1Input
    global zsl_1input
    global d_tw
    global d_zsl
    global l_tw
    global l_zsl
    global l_dns
    global l_znrz
    l_tw = []
    l_zsl = []
    l_dns = []
    l_znrz = []

    print(count)

    # dodanie do listy pierwszego wiersza pól
    try:
        l_tw.append(float(pol_usr(tw_1Input.get())))
    except:
        print('Incorrect temp input')

    try:
        l_zsl.append(float(zsl_1input.get()))
    except:
        print('Incorrect salinity input')

    # dodanie do listy pól użytkownika
    for i in d_tw.values():
        try:
            l_tw.append(float(pol_usr(i.get())))
        except:
            print('Incorrect temp input')
    for i in d_zsl.values():
        try:
            l_zsl.append(float(pol_usr(i.get())))
        except:
            print('Incorrect salinity input')
    # wyświetlenie list
    print(f'Lista temperatur: {l_tw}')
    print(f'Lista zasolenia: {l_zsl}')

    # obliczenia dla wartości w liście gęstosci
    for i in range(count - 1):
        l_dns.append(density(l_tw[i], l_zsl[i]))
    print(f'Lista gęstości: {l_dns}')

    for i in range(count - 1):
        dns = tkinter.Label(root, text=round(l_dns[i], 3))
        dns.grid(column=4, row=i + 2)

    # obliczenia dla wartości w liście zanurzeń
    l_znrz = draughts(l_dns, znrz0_input.get())
    print(f'Lista zanurzeń: {l_znrz}')

    for i in range(count - 1):
        znrz = tkinter.Label(root, text=round(l_znrz[i], 3))
        znrz.grid(column=5, row=i + 2)


# wazne stale
count = 2
znrz0 = 0

# listy
l_tw = []  # temperatura wody
l_zsl = []  # zasolenie
l_dns = []  # density
l_znrz = []  # zanurzenie

# slowniki
d_tw = {}  # słownik na pola temperatury
d_zsl = {}  # słownik na pola zasolenia

# program
root = tkinter.Tk()
root.title('Kalkulator zanurzeń')

# top lable
znrz0_lable = tkinter.Label(root, text='Zanurzenie początkowe')
tw_1Label = tkinter.Label(root, text='Temperatura wody')
zsl_1Lable = tkinter.Label(root, text='Zasolenie')
g_wody1Lable = tkinter.Label(root, text='Gęstość wody')
z_statku1Lable = tkinter.Label(root, text='Zanurzenie statku')

# first side lable
akwnLable = tkinter.Label(root, text='Akwen 1')

# pola dane 1
znrz0_input = tkinter.Entry(root)
tw_1Input = tkinter.Entry(root)
zsl_1input = tkinter.Entry(root)

# guzik dodania więcej akwenów
btn_add = tkinter.Button(root, text='Dodaj akwen.', padx=20, command=btnpress)

# guzik kalkuluj
btncalculate = tkinter.Button(root, text='Oblicz', padx=20, command=btncalc)

# packing
# input fields
znrz0_input.grid(column=2, row=0)
tw_1Input.grid(column=2, row=2)
zsl_1input.grid(column=3, row=2)
# lable
znrz0_lable.grid(column=1, row=0)
akwnLable.grid(column=1, row=2)
tw_1Label.grid(column=2, row=1)
zsl_1Lable.grid(column=3, row=1)
g_wody1Lable.grid(column=4, row=1)
z_statku1Lable.grid(column=5, row=1)

# guziki
btn_add.grid(column=1, row=1)
btncalculate.grid(column=4, columnspan=2, ipadx=50, row=50)

# petla
root.mainloop()
