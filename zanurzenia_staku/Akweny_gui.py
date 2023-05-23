import tkinter
import datetime
import os
from tkinter import messagebox, ttk


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

    # zmienna do słownika
    key = f'num{count - 3}'
    # dopisanie do zmiennych 0
    var_1 = tkinter.StringVar(root, value='0')
    var_2 = tkinter.StringVar(root, value='0')
    # pola tekstowe
    d_tw[key] = tkinter.Entry(root, validate='key', width=16, textvariable=var_1)
    d_zsl[key] = tkinter.Entry(root, width=16, textvariable=var_2)

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
            messagebox.showerror(message='Niepoprawna temperatura', title='Błąd')
    # dodanie do listy zasolenia
    for i in d_zsl.values():
        try:
            l_zsl.append(float(pol_usr(i.get())))
        except:
            print(f'Niepoprawne zasolenie - wiersz {i}')
            messagebox.showerror(message='Niepoprawne zasolenie', title='Błąd')

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
    global tmp_in, dst_in, slc_dst_wnk, slc_dst, slc_tmp, slc_tmp_wnk, converter
    converter = tkinter.Toplevel()
    converter.title('Konverter')

    # lable
    lbl_tmp = tkinter.Label(converter, text='Temperatura', padx=20)
    lbl_len = tkinter.Label(converter, text='Długość', padx=20)
    lbl_vl = tkinter.Label(converter, text='Wartość', padx=20)
    lbl_jdnst = tkinter.Label(converter, text='Jednostka', padx=20)
    lbl_jdnstw = tkinter.Label(converter, text='Jednostka wyniku', padx=20)
    lbl_rslt = tkinter.Label(converter, text='Wynik', padx=20)
    # wyswietlenie lable
    lbl_tmp.grid(column=1, row=3)
    lbl_len.grid(column=1, row=4)
    lbl_vl.grid(column=2, row=2)
    lbl_jdnst.grid(column=3, row=2)
    lbl_jdnstw.grid(column=5, row=2)
    lbl_rslt.grid(column=4, row=2)

    # select
    # temperatura
    slc_tmp = tkinter.StringVar()
    tmp_selected = ttk.Combobox(converter, width=15, textvariable=slc_tmp)
    tmp_selected['values'] = ('Celsjusz', 'Fahrenheit', 'Kelvin')
    # odleglosc
    slc_dst = tkinter.StringVar()
    dst_selected = ttk.Combobox(converter, width=15, textvariable=slc_dst)
    dst_selected['values'] = ('Metry', 'Stopy', 'Mile Morskie', 'Kilometry')
    # temperatura wynik
    slc_tmp_wnk = tkinter.StringVar()
    tmp_selected_wnk = ttk.Combobox(converter, width=15, textvariable=slc_tmp_wnk)
    tmp_selected_wnk['values'] = ('Celsjusz', 'Fahrenheit', 'Kelvin')
    # odleglosc wynik
    slc_dst_wnk = tkinter.StringVar()
    dst_selected_wnk = ttk.Combobox(converter, width=15, textvariable=slc_dst_wnk)
    dst_selected_wnk['values'] = ('Metry', 'Stopy', 'Mile Morskie', 'Kilometry')
    # wyswietlenie select
    tmp_selected.grid(column=3, row=3)
    tmp_selected_wnk.grid(column=5, row=3)
    dst_selected.grid(column=3, row=4)
    dst_selected_wnk.grid(column=5, row=4)

    # input fields
    tmp_in = tkinter.Entry(converter)
    dst_in = tkinter.Entry(converter)
    # wyswietlenie in fields
    tmp_in.grid(column=2, row=3)
    dst_in.grid(column=2, row=4)

    # buttons
    clc_tmp = tkinter.Button(converter, text='O B L I C Z', command=cnvrt_tmp_clc)
    clc_dst = tkinter.Button(converter, text='O B L I C Z', command=cnvrt_dst_clc)
    # wyswietlenie buttons
    clc_tmp.grid(column=6, row=3)
    clc_dst.grid(column=6, row=4)

    # dodatatkowe
    dst_lbl = tkinter.Label(converter, text='        ', width=20)
    dst_lbl.grid(column=4, row=4)
    tmp_lbl = tkinter.Label(converter, text='        ', width=20)
    tmp_lbl.grid(column=4, row=5)


def cnvrt_tmp_clc():
    global tmp_in, dst_in, slc_dst_wnk, slc_dst, slc_tmp, slc_tmp_wnk, converter
    tmp = None
    try:
        tmp_u_in = float(tmp_in.get())
    except:
        print('Błędna wartość temperatury.')
        messagebox.showerror(message='Niepoprawna temperatura', title='Błąd')
    print(slc_tmp.get())
    print(slc_tmp_wnk.get())

    if slc_tmp.get() == 'Celsjusz':
        if slc_tmp_wnk.get() == 'Celsjusz':
            tmp = tmp_u_in
        elif slc_tmp_wnk.get() == 'Fahrenheit':
            tmp = tmp_u_in * 9 / 5 + 32
        elif slc_tmp_wnk.get() == 'Kelvin':
            tmp = tmp_u_in + 273.15
    elif slc_tmp.get() == 'Fahrenheit':
        if slc_tmp_wnk.get() == 'Fahrenheit':
            tmp = tmp_u_in
        elif slc_tmp_wnk.get() == 'Celsjusz':
            tmp = (tmp_u_in-32) * 5 / 9
        elif slc_tmp_wnk.get() == 'Kelvin':
            tmp = (tmp_u_in-32) * 5 / 9 + 273.15
    elif slc_tmp.get() == 'Kelvin':
        if slc_tmp_wnk.get() == 'Kelvin':
            tmp = tmp_u_in
        elif slc_tmp_wnk.get() == 'Celsjusz':
            tmp = tmp_u_in - 273.15
        elif slc_tmp_wnk.get() == 'Fahrenheit':
            tmp = (tmp_u_in - 273.15) * 9 / 5 + 32
    print(tmp)
    # wyswietlenie wyniku
    tmp_lbl = tkinter.Label(converter, text=tmp, width=20)
    tmp_lbl.grid(column=4, row=3)


def cnvrt_dst_clc():
    global tmp_in, dst_in, slc_dst_wnk, slc_dst, slc_tmp, slc_tmp_wnk, converter
    dst = None
    try:
        dst_u_in = float(dst_in.get())
    except:
        print('Błędna wartość odległości')
        messagebox.showerror(message='Niepoprawna odległość', title='Błąd')
    # z metrow na inne
    if slc_dst.get() == 'Metry':
        if slc_dst_wnk.get() == 'Metry':
            dst = dst_u_in
        elif slc_dst_wnk.get() == 'Kilometry':
            dst = dst_u_in / 1000
        elif slc_dst_wnk.get() == 'Stopy':
            dst = dst_u_in * 3.2808399
        elif slc_dst_wnk.get() == 'Mile Morskie':
            dst = dst_u_in * 0.00054
    # ze stop na inne
    elif slc_dst.get() == 'Stopy':
        if slc_dst_wnk.get() == 'Stopy':
            dst = dst_u_in
        elif slc_dst_wnk.get() == 'Metry':
            dst = dst_u_in * 0.3048
        elif slc_dst_wnk.get() == 'Mile Morskie':
            dst = dst_u_in * 0.00016459199974982016
        elif slc_dst_wnk.get() == 'Kilometry':
            dst = dst_u_in * 0.000304799999536704
    # z mil na inne
    elif slc_dst.get() == 'Mile Morskie':
        if slc_dst_wnk.get() == 'Mile Morskie':
            dst = dst_u_in
        elif slc_dst_wnk.get == 'Kilometry':
            dst = dst_u_in * 1.851851851851851852
        elif slc_dst_wnk.get() == 'Metry':
            dst = dst_u_in * 1851.851851851851852
        elif slc_dst_wnk.get() == 'Stopy':
            dst = dst_u_in * 6075.6294444444444449304948
    # z kilemetrow na inne
    elif slc_dst.get() == 'Kilometry':
        if slc_dst_wnk.get() == 'Kilometry':
            dst = dst_u_in
        elif slc_dst_wnk.get() == 'Mile Morskie':
            dst = dst_u_in * 0.54
        elif slc_dst_wnk.get() == 'Metry':
            dst = dst_u_in * 1000
        elif slc_dst_wnk.get() == 'Stopy':
            dst = dst_u_in / 3280.8399

    # wyswietlenie wyniku
    dst = round(dst, 6)
    dst_lbl = tkinter.Label(converter, text=dst, width=20)
    dst_lbl.grid(column=4, row=4)


# --- MAIN CODE ---
# wazne stale
count = 2
znrz0 = 0

# stale converter
tmp_in = None
dst_in = None
slc_dst_wnk = None
slc_dst = None
slc_tmp = None
slc_tmp_wnk = None
converter = None

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

# str variable - podstawowa wartosc
var_znrz = tkinter.StringVar(root, value='0')
var_tw = tkinter.StringVar(root, value='0')
var_zsl = tkinter.StringVar(root, value='0')
# pola dane 1
znrz0_input = tkinter.Entry(root, width=16, textvariable=var_znrz)
tw_1Input = tkinter.Entry(root, width=16, textvariable=var_tw)
zsl_1input = tkinter.Entry(root, width=16, textvariable=var_zsl)

#guziki
# guzik dodania więcej akwenów
btn_add = tkinter.Button(root, text='DODAJ AKWEN', padx=10, command=btnpress)
# guzik kalkuluj
btncalculate = tkinter.Button(root, text=' O B L I C Z  ', padx=15, command=btncalc)
# guzik zapisz
btn_save = tkinter.Button(root, text='ZAPISZ', padx=24, command=save)
# guzik otworz
btn_open = tkinter.Button(root, text='OTWÓRZ', padx=25, command=open_log)
# guzik converter
btn_cnvrt = tkinter.Button(root, text='Konwerter', padx=20, command=converter_window)

# packing
# input fields
znrz0_input.grid(column=5, row=2)
tw_1Input.grid(column=2, row=2)
zsl_1input.grid(column=3, row=2)
# lable

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
btn_cnvrt.grid(column=1, row=51)

# petla
root.mainloop()

# Filip Kozlowski
