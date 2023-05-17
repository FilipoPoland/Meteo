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


root = tkinter.Tk()



root.mainloop()
