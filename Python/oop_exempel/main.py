import time

from repo.recept_budapest import Recept_Pa_En_Budapest_Rulle as recept


def main():
    en_lista_med_kakor = []

    print('Nu ska vi baka!')
    print(f'Plocka fram receptet "{recept.__doc__}"')

    # Anropar en statisk metod i klassen
    antal = recept.fraga_om_antal_rullar()

    # Skapar en instans av receptet (klassen)
    nummer = 1
    while nummer <= antal:
        # en_lista_med_kakor.append(recept(nummer, datetime.datetime.now()))
        en_lista_med_kakor.append(recept(nummer))
        kaka = en_lista_med_kakor[nummer - 1]
        nummer += 1

        print(f'Nu bakar vi kaka nr. {kaka.kakans_nummer}')
        if kaka.antal_rullar > 1:
            print(f'\nDu behöver följande ingredienser för att baka {kaka.antal_rullar} st Budapestrullar:')
        else:
            print(f'\nDu behöver följande ingredienser för att baka {kaka.antal_rullar} st Budapestrulle:')
        kaka.skriv_ut_ingredienserna()

        kaka.starta_ugnen()
        torra_ingredienser = kaka.blanda_torra_ingredisenser()

        smeten = kaka.vispa(torra_ingredienser)

        kaka.spritsa(smeten)

        kaka.gradda()
        print('>>> Kakan gräddas <<<')
        time.sleep(2)

        tartbotten = kaka.ta_ut_ur_ugnen()

        kaka.stryk_pa_gradde(tartbotten)

        kaka.dela_rulltartan()

    print('\nDessa kakor har du bakat:')
    for kaka1 in en_lista_med_kakor:
        kaka1.skriv_ut_tid_och_nummer()

    print('\n\nHoppas det smakar bra;)')


if __name__ == '__main__':
    main()
