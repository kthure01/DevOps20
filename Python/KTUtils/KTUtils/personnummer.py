import re


def compute_check_digit_pnr(s):
    if not bool(re.search("^\d{9}$", s)):
        return False
    return (10 - (sum(map(lambda x: x % 10 + int(x / 10),
                          map(lambda x, y: x * y, map(int, s), [2, 1] * 4 + [2]))) % 10)) % 10


def swedish_pnr_check_digit(s):
    """Return check digit associated with partial personnummer s or None.

    Accept partial personnummer strings in the format
    [åå]ÅÅMMDD[-+]NNN.  All non-digits are scrubbed and only the last
    9 digits (ÅÅMMDDNNN) are used when calculating the check digit C
    using the Luhn algorithm.

    None is returned when there are too few digits.  None rather than
    False, since it is harder to interpret as 0.

    >>> swedish_pnr_check_digit("19811218-987")
    6
    >>> swedish_pnr_check_digit("19811218+987")
    6
    >>> swedish_pnr_check_digit("811218+987")
    6
    >>> swedish_pnr_check_digit("811218987")
    6
    >>> swedish_pnr_check_digit("81121898") == None
    True
    >>> swedish_pnr_check_digit("818181818")
    1
    >>> check_swedish_pnr("8181818181")
    True
    """

    for d in re.sub(r'\D', '', s)[-9:]:
        print(d)




    digits = [int(d) for d in re.sub(r'\D', '', s)][-9:]
    if len(digits) != 9:
        return None
    even_digitsum = sum(x if x < 5 else x - 9 for x in digits[::2])
    check_digit = sum(digits, even_digitsum) % 10
    return 10 - check_digit if check_digit else 0


swedish_pnr_check_digit('196304152959')
'''
Beräkning av kontrollsiffra

För att beräkna kontrollsiffran är förfarandet likvärdigt, med skillnaden att man multiplicerar ömsom med 2 och ömsom med 1 (det vill säga att man börjar att multiplicera den sista siffran med 2, och inte med 1 som i fallet vid kontroll). Den erhållna summan dras därefter ifrån närmast större 10-tal, varvid kontrollsiffran erhålles.

För att beräkna kontrollsiffran för det niosiffriga personnumret 811218-987 erhålles följande produkter:

   8  1 1 2 1 8  9 8  7
*  2  1 2 1 2 1  2 1  2
-------------------------
   ^  ^ ^ ^ ^ ^  ^ ^  
  16  1 2 2 2 8 18 8 14

Tvåsiffriga produkter splittras upp i ensiffriga tal. Siffrorna summeras därefter:

1 + 6 + 1 + 2 + 2 + 2 + 8 + 1 + 8 + 8 + 1 + 4 = 44 {\displaystyle 1+6+1+2+2+2+8+1+8+8+1+4=44} {\displaystyle 1+6+1+2+2+2+8+1+8+8+1+4=44}

Kontrollsiffran erhålls genom att detta tal subtraheras från närmast högre tiotal. Om differensen är 10 blir kontrollsiffran 0[1].

50 − 44 = 6 {\displaystyle 50-44=6} {\displaystyle 50-44=6}

Den avslutande kontrollsiffran blir således en sexa och det tiosiffriga personnumret blir 811218-9876. 


'''