import re


def check_pnr(s):
    if not bool(re.search("^\d{10}$", s)):
        return False
    return sum(map(lambda x: x % 10 + int(x / 10),
                   map(lambda x, y: x * y, map(int, s), [2, 1] * 5))) % 10 == 0


# Alternativ och något mer generell rutin.
def check_swedish_pnr(personnummer):
    """Return True when personnummer passes the Luhn test, else False.

    Accept personnummer strings in the format [åå]ÅÅMMDD[-+]NNNC.  All
    non-digits are scrubbed and only the last 10 digits (ÅÅMMDDNNNC)
    are used when performing the Luhn test.

    >>> check_swedish_pnr("19811218+9876")
    True
    >>> check_swedish_pnr("811218-9876")
    True
    >>> check_swedish_pnr("8112189876")
    True

    Number the sequence of digits ÅÅMMDDNNNC left to right from 10 to
    1.  The even numbered digits should be multiplied by 2, but when
    the product is >= 10 use the digit sum of the product. Odd
    numbered digits are summed as they are.  Two cases when
    multiplying

       1. 2*d < 10 ---> d + d
       2. 2*d >= 10 use the respective digit sum ---> d + d - 9
       --->
       sum(all_digits, even_digits)
    """
    digits = [int(d) for d in re.sub(r'\D', '', personnummer)][-10:]
    if len(digits) != 10:
        return False
    even_digitsum = sum(x if x < 5 else x - 9 for x in digits[::2])
    return 0 == sum(digits, even_digitsum) % 10


'''
Kontroll av nummer

Vid kontroll av koden, inklusive kontrollsiffra, fungerar algoritmen på så sätt att med start från den sista siffran i koden (den minst signifikanta siffran), det vill säga kontrollsiffran, multipliceras siffrorna ömsom med 1 och ömsom med 2. Skulle något tal vid en sådan multiplikation bli större än 9 ersätts talet med dess siffersumma (eller, likvärdigt, med talet subtraherat med 9). Därefter summeras talen. Om den erhållna summan är jämnt delbar med 10 så är kontrollsiffran korrekt.

Exempel på personnummer 811218-9876:

   8  1 1 2 1 8  9 8  7 6
*  2  1 2 1 2 1  2 1  2 1
-------------------------
   ^  ^ ^ ^ ^ ^  ^ ^  ^ 
  16  1 2 2 2 8 18 8 14 6

Tvåsiffriga produkter splittras upp i ensiffriga tal. Siffrorna summeras därefter:

1 + 6 + 1 + 2 + 2 + 2 + 8 + 1 + 8 + 8 + 1 + 4 + 6 = 50 {\displaystyle 1+6+1+2+2+2+8+1+8+8+1+4+6=50} {\displaystyle 1+6+1+2+2+2+8+1+8+8+1+4+6=50}

Denna summa är delbar med 10 och sålunda har vi inte upptäckt något fel i numret. 
'''

'''
SEB 5000-5999 00000xxxxxxC 11-modul

1.1 10-modulmetoden
Kontrollsiffran i ett 10-modulnummerbegrepp är dess sista siffra:
Kontroll av nummer, som har kontrollsiffra:
Sista siffran (= kontrollsiffran) multipliceras med 1, näst sista med 2, 3:e från
slutet åter med 1, 4:e från slutet åter med 2 etc., dvs. alla siffror multipliceras
omväxlande med 1 resp. 2 bakifrån räknat. (Faktorerna 1 och 2 kallas ”vikter”.)
Av nu framräknade produkter modifieras alla som blivit 2-siffriga genom
subtraktion med 9 (alternativt att deras 2 siffror adderas med varandra till ett 1-
siffrigt tal).
Samtliga framräknade produkter (2-siffriga dock modifierade till 1-siffriga enligt
ovan) summeras – om summan är ett med 10 jämnt delbart tal, är numret
korrekt.
Exempel:
Ett 13-siffrigt kontonummer ska kontrolleras:
Kontonr: 3 3 1 6 8 1 2 0 5 7 4 9 2
Vikter: 1 2 1 2 1 2 1 2 1 2 1 2 1
Prod: 3 6 1 12 8 2 2 0 5 14 4 18 2
Modif: -9 -9 -9
Uträkn: 3 +6 +1 +3 +8 +2 +2 +0 +5 +5 +4 +9 +2 = 50;
Summan 50 slutar med 0; Numret är godkänt
Uträkning av kontrollsiffra för konstruktion av 10-modulnummer:
Sätt slutsiffran (kontrollsiffran) preliminärt = 0 och tillämpa beräkningsmetoden
under a) ovan.
Om framräknad produktsumma (efter modifikation av 2-siffriga produkter till 1-
siffriga) är jämnt delbar med 10, behålles nollan som kontrollsiffra; annars ersätts
den av skillnaden mellan 10 och resten från divisionen.


1.2 11-modulmetoden
Kontrollsiffran i ett 11-modulnummerbegrepp är dess sista siffra (ev. dess 2 sista
siffror – se anm. Nederst under b) nedan)
Kontroll av nummer, som har kontrollsiffra
Sista siffran (= kontrollsiffran) multipliceras med 1, näst sista med 2, nästnäst
sista med 3 etc. upp till max 10. Om numret är längre än 10 siffror, återupptas
multiplikation med 1, 2, 3 etc. fr.o.m. 11:e (21:a etc.) siffran från slutet.
(Faktorerna 1 – 10 kallas ”vikter”.)
Enligt ovan framräknade produkter summeras – om summan är ett med 11 jämnt
delbart tal, är numret korrekt.
Exempel:
Ett 13-siffrigt kontonummer ska kontrolleras:
Kontonr: 1 9 1 2 7 6 3 6 0 8 9 5 7
Vikter: 3 2 1 10 9 8 7 6 5 4 3 2 1
Uträkn: 3 +18 +1 +20 +63 +48 +21 +36 +0 +32 +27 +10 +7=286;
286/11=26; Numret är godkänt
Uträkning av kontrollsiffra för konstruktion av 11-modulnummer:
Sätt slutsiffran (kontrollsiffran) preliminärt = 0 och tillämpa beräkningsmetoden
under a) ovan.
Om framräknad produktsumma är jämnt delbar med 11, behålles nollan som
kontrollsiffra; annars ersätts den av skillnaden mellan 11 och resten från
divisionen såvida inte denna skillnad blir 10 (resten blev = 1). I sistnämnda fall är
grundnumret oanvändbart som stomme för ett 11-modulkontrollerbart nummer.
Anm: 11-modulmetoden innebär att i genomsnitt vart 11:e nummer i en svit av
”grundnummer” (nr utan kontrollsiffra), är oanvändbart för konstruktion av
11-modulnummer. I fall, då effekten med oanvändbara grundnummer ej kan
accepteras (ex vis om vissa av grundnumrets olika sifferpositioner ska ha
specifika betydelser beroende av värdet i dem), är den vanligaste metoden att
kringgå detta problem följande: GRUNDnumrets sista siffra ges
utgångsvärdet = 0.
I ovannämnda ”felfall”, då framräknad kontrollsiffra skulle bli 10, sätter man
den i stället till 8 och ändrar grundnumrets slutnolla till 1 (som ju på grund
av ”vikten” 2 får 11-moduluträkningsvärdet 2; 2+8=10).
Man kan även uttrycka detta som att det kompletta 11-modulnumret har 2
kontrollsifferpositioner i slutet, som kan anta värden i intervallet 00-09 eller
värdet 18.
'''