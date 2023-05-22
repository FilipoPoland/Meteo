while True:

    S = input('Jakie jest zasolenie wody?\n')
    Tw = input('Jaka jest temperatura wody?\n')
    # gestosc umowna
    Pu = (28.1522 - (0.0735 * float(Tw)) - (0.00469 * (float(Tw) ** 2)) + (0.802 - (0.002 * float(Tw))) *
          (float(S) - 35.0))
    # gestosc
    r = ((Pu / 1000) + 1)  # gestosc
    # pomocnicza linia opisuje pozniejsza wartosc r
    print('Gęstość wody to', r)
    again = input('Aby ponowić proces należy wprowadzić "y". Aby zakończyć program enter.')
    if 'y' in again:
        continue
    else:
        break
print('Dziękuję za użycie mojego programu.')
input('Aby zakończyć program należy kliknąć enter.')
