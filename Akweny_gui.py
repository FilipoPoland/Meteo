import tkinter


def density(water_temp, salinity):
    pu = (28.1522 - (0.0735 * float(water_temp)) - (0.00469 * (float(water_temp) ** 2)) +
          (0.802 - (0.002 * float(water_temp))) * (float(salinity) - 35.0))
    g = float(pu) / 1000 + 1
    return g


def draughts(densty_list, zanurzenie0):
    draughts_list = []
    for i in densty_list:
        zanurzenie = ((float(densty_list[i])) / float(densty_list[i+1])) * float(zanurzenie0)
        draughts_list.append(zanurzenie)
        zanurzenie0 = zanurzenie
    return draughts_list


def pol_usr(get_input):
    fr_cptr = get_input.replace(',', '.')
    fr_cptr = fr_cptr.replace(' ', '')
    return fr_cptr


def btnclck():
    counting()

    # akwen nazwa
    lbl = tkinter.Label(text=f'Akwen {count-1}')
    # temperatura wody pole do danych
    tw_input = tkinter.Entry(root, )
    # zasolenie pole danych
    zsl_input = tkinter.Entry(root, )

    # akwen nazwa
    lbl.grid(column=1, row=count)
    # temperatura wody
    tw_input.grid(column=2, row=count)
    # zasolenie
    zsl_input.grid(column=3, row=count)


def counting():
    global count
    count += 1
    return count


def btncalc():
    print(count)
    tw1 = float(tw_1Input.get())
    zsl1 = float(zsl_1input.get())
    print(tw1, zsl1)




# wazne stale
count = 2
#listy
l_tw = []
l_zsl = []

# program
root = tkinter.Tk()
root.title('Kalkulator zanurzeń')

# top lable
tw_1Label = tkinter.Label(root, text='Temperatura wody')
zsl_1Lable = tkinter.Label(root, text='Zasolenie')

# first side lable
akwnLable = tkinter.Label(root, text='Akwen 1')

# pola dane 1
tw_1Input = tkinter.Entry(root, )
zsl_1input = tkinter.Entry(root, )

# guzik dodania więcej akwenów
btnad = tkinter.Button(root, text='Dodaj akwen.', padx=20, command=btnclck)

# guzik kalkuluj
btncalculate = tkinter.Button(root, text='Oblicz', padx=20, command=btncalc)

# packing
akwnLable.grid(column=1, row=2)
tw_1Label.grid(column=2, row=1)
tw_1Input.grid(column=2, row=2)
zsl_1Lable.grid(column=3, row=1)
zsl_1input.grid(column=3, row=2)
btnad.grid(column=1, row=50)
btncalculate.grid(column=4, row=50)



# petla
root.mainloop()
