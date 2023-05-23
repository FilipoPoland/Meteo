import tkinter
import datetime
import os
from tkinter import messagebox


def density(water_temp, salinity):
    pu = (28.1522 - (0.0735 * float(water_temp)) - (0.00469 * (float(water_temp) ** 2)) +
          (0.802 - (0.002 * float(water_temp))) * (float(salinity) - 35.0))
    g = float(pu) / 1000 + 1
    return g


def draughts(densty_list, zanurzenie0):
    global l_znrz
    l_znrz = []
    try:
        znrz = float(pol_usr(zanurzenie0))
        l_znrz.append(znrz)
    except:
        print('Podano złą wartość zanurzenia początkowego.')
        messagebox.showerror(message='Niepoprawne zanurzenie', title='Błąd')

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
    d_tw[key] = tkinter.Entry(root, validate='key', width=16)
    d_zsl[key] = tkinter.Entry(root, width=16)

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
    global tw_1Input, zsl_1input, znrz0
    global d_tw, d_zsl
    global l_tw, l_zsl, l_dns, l_znrz

    # reset list
    l_tw = []
    l_zsl = []
    l_dns = []

    # dodanie do listy pierwszego wiersza pól
    # dodanie temperatury 1 do listy
    try:
        l_tw.append(float(pol_usr(tw_1Input.get())))
    except:
        print('Incorrect temp input')
        messagebox.showerror(message='Niepoprawna temperatura', title='Błąd')
    # dodanie zasolenia 1 do listy
    try:
        l_zsl.append(float(zsl_1input.get()))
    except:
        print('Incorrect salinity input')
        messagebox.showerror(message='Niepoprawne zasolenie', title='Błąd')

    # dodanie do listy pól użytkownika
    # dodanie do listy temperatur
    for i in d_tw.values():
        try:
            l_tw.append(float(pol_usr(i.get())))
        except:
            print(f'Niepoprawne zasolenie {i}')
            messagebox.showerror(message=f'Niepoprawna temperatura', title='Błąd')
    # dodanie do listy zasolenia
    for i in d_zsl.values():
        try:
            l_zsl.append(float(pol_usr(i.get())))
        except:
            print(f'Niepoprawne zasolenie - wiersz {i}')
            messagebox.showerror(message=f'Niepoprawne zasolenie', title='Błąd')

    # wyświetlenie list
    print(f'Lista temperatur: {l_tw}')
    print(f'Lista zasolenia: {l_zsl}')

    # obliczenia dla wartości w liście gęstosci
    for i in range(count - 1):
        l_dns.append(density(l_tw[i], l_zsl[i]))
    print(f'Lista gęstości: {l_dns}')

    # wyswietlenie gestosci
    for i in range(count - 1):
        dns = tkinter.Label(root, text=round(l_dns[i], 4))
        dns.grid(column=4, row=i + 2)

    # lista zanurzenia
    l_znrz = draughts(l_dns, znrz0_input.get())
    print(f'Lista zanurzeń: {l_znrz}')

    # wyswietlenie zanurzen
    for i in range(count - 2):
        znrz = tkinter.Label(root, text=round(l_znrz[i + 1], 3))
        znrz.grid(column=5, row=i + 3)


def save():
    time_stmp = str(datetime.datetime.now())
    print(time_stmp)
    with open('../zanurzenia_logs.txt', 'a') as file:
        file.write('\n' + str(time_stmp) + '\n'
                   + 'Lista temperatur wody:\n' + str(l_tw) + '\n'
                   + 'Lista zasolen wody: \n' + str(l_zsl) + '\n'
                   + 'Lista gestosci wody: \n' + str(l_dns) + '\n'
                   + 'Lista zanurzen statku:\n' + str(l_znrz) + '\n')


def open_log():
    os.system('start zanurzenia_logs.txt')


def converter_window():
    converter = tkinter.Toplevel()
    converter.title('Konverter')
    # top lable
    lbl_tmp = tkinter.Label()
    lbl_len


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
# znrz0_lable = tkinter.Label(root, text='Zanurzenie początkowe')
tw_1Label = tkinter.Label(root, text='Temperatura wody')
zsl_1Lable = tkinter.Label(root, text='Zasolenie')
g_wody1Lable = tkinter.Label(root, text='Gęstość wody')
z_statku1Lable = tkinter.Label(root, text='Zanurzenie statku')

# first side lable
akwnLable = tkinter.Label(root, text='Akwen 1')

# pola dane 1
znrz0_input = tkinter.Entry(root, width=16)
tw_1Input = tkinter.Entry(root, width=16)
zsl_1input = tkinter.Entry(root, width=16)

#guziki
# guzik dodania więcej akwenów
btn_add = tkinter.Button(root, text='DODAJ AKWEN', padx=10, command=btnpress)
# guzik kalkuluj
btncalculate = tkinter.Button(root, text=' O B L I C Z  ', padx=15, command=btncalc)
# guzik zapisz
btn_save = tkinter.Button(root, text='ZAPISZ', padx=24, command=save)
# guzik otworz
btn_open = tkinter.Button(root, text='OTWÓRZ', padx=25, command=open_log)

# packing
# input fields
znrz0_input.grid(column=5, row=2)
tw_1Input.grid(column=2, row=2)
zsl_1input.grid(column=3, row=2)
# lable
# znrz0_lable.grid(column=1, row=0)
akwnLable.grid(column=1, row=2)
tw_1Label.grid(column=2, row=1)
zsl_1Lable.grid(column=3, row=1)
g_wody1Lable.grid(column=4, row=1)
z_statku1Lable.grid(column=5, row=1)
# guziki
btn_add.grid(column=1, row=1)
btncalculate.grid(column=4, columnspan=2, ipadx=50, row=50)
btn_save.grid(column=4, row=51)
btn_open.grid(column=5, row=51)

# petla
root.mainloop()
