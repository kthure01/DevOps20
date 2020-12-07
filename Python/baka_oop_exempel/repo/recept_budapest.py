import datetime

from repo.fastutrustning import FastUtrustning
from repo.los_utrustning import LosUtrustningIKoket


# För att kunna baka så behöver vi lite övrig utrustning från köket.
# Denna utrustning "ärver (inherit)" vi in från 2 klasser.
class ReceptPaEnBudapestrulle(FastUtrustning, LosUtrustningIKoket):
    """Detta är ett recept på Budapestrulle"""

    # Grundrecept för att baka en rulle
    antal_rullar = 1
    strosocker = 90 + 90
    hasselnotsmjol = 70
    majsstarkelse = 35
    aggvita = 125
    gradde = 300
    apelsin = 2
    farska_hallon = 2
    mork_choklad = 100

    ugns_temperatur = 170

    def __init__(self, kakans_nummer):
        self.kakans_nummer = kakans_nummer
        self.kakan_borjar_bakas = datetime.datetime.now()

    # Denna metod är nåbar utan instantiering av klassen
    @staticmethod
    def fraga_om_antal_rullar():
        print('OBS! Det tar 2 sekunder att baka varje tårta;)')
        return int(input('Hur många rullar vill du baka? [1]:') or '1')

    def skriv_ut_ingredienserna(self):
        print(f'Kaka nr. {self.kakans_nummer} som började bakas kl. {self.kakan_borjar_bakas}')
        print(f'Socker: {self.strosocker}g')
        print(f'Hasselnötsmjöl: {self.hasselnotsmjol}g')
        print(f'Majsstärkelse: {self.majsstarkelse}g')
        print(f'Äggvita: {self.aggvita}g')
        print(f'Grädde: {self.gradde}g')
        print(f'Apelsin: {self.apelsin}g')
        print(f'Färska hallon: {self.farska_hallon}g')
        print(f'Mörk choklad: {self.mork_choklad}g')

    def starta_ugnen(self):
        print(f'\n1) Sätt {self.ugn} på {self.ugns_temperatur} grader.')
        self.stall_in_ugns_temparatur(self.ugns_temperatur)
        print(f'   Ugnen är nu {self.ugnstemperatur} grader.')
        print(f'   Lägg {self.bakplatspapper} på {self.bakplat}.')

    # Returnerar blandningen av de torra ingredienserna
    def blanda_torra_ingredisenser(self):
        print(f'\n2) Blanda hälften av strösockret ({self.strosocker / 2}g),', end=' ')
        print(f'hasselnötsmjöl ({self.hasselnotsmjol}g) och maizena ({self.majsstarkelse}g)', end=' ')
        print(f'i {self.bunke}.')

        return 'torra ingredienserna'

    # Returnerar den färdiga smeten till botten
    def vispa(self, torra_ingredienser):
        print(f'\n3) Vispa äggvita ({self.aggvita}g) fluffigt och fast, tillsätt lite i taget')
        print(f'   resten av strösockret ({self.strosocker / 2}g) och vispa till en fast maräng.')
        print(f'   Blanda i de {torra_ingredienser} med {self.slickepott} och')
        print(f'   blanda försiktigt tills det är välblandat.')

        return 'smeten'

    def spritsa(self, smet):
        print(f'\n4) Spritsa ut med {self.sprits_och_tyll} mellan 17-18 plåtlånga strängar')
        print(f'   tätt på {self.bakplatspapper} eller tills {smet} tar slut.')

    def gradda(self):
        print(f'\n5) Grädda mitt i {self.ugn} på {self.ugnstemperatur} grader i 20 min,')
        print(f'   lufta {self.ugn} några sekunder och baka ytterligare 2 min.')

    # Returnerar den färdigbakade botten
    def ta_ut_ur_ugnen(self):
        print(f'\n6) Ta ut botten ur ugnen och låt svalna,')
        print(f'   lägg på ett {self.bakplatspapper} på botten och vänd')
        print(f'   den så att du har undersidan uppåt.')

        return 'botten'

    def stryk_pa_gradde(self, botten):
        print(f'\n7) Stryk på ett tunt lager {self.vispa_gradde()} på {botten}, sprid ut små apelsinbitar')
        print(f'   och delade hallonbitar, rulla ihop {botten} till en rulle.')

    def dela_rulltartan(self):
        if self.antal_rullar < 2:
            print(f'\n8) Dela din rulltårta på längden till 8 bakelser,')
        else:
            print(f'\n8) Dela varje rulltårta på längden till 8 bakelser (totalt {self.antal_rullar * 8} bakelser),')

        print(f'   ringla över lite {self.smalt_choklad()} och pudra på florsocker.')

    # Returnerar vispad grädde
    def vispa_gradde(self):
        print('>>> Vispar grädden <<<')
        return 'vispad grädde'

    # Returnerar smält choklad
    def smalt_choklad(self):
        print('>>> Smälter choklad <<<')
        return 'smält mörk choklad'

    def skriv_ut_tid_och_nummer(self):
        print(f'Kaka nr: {self.kakans_nummer} är klar. Den bakades: {self.kakan_borjar_bakas}. Objektid: {id(self)}')
