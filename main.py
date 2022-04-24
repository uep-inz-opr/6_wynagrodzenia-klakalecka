import math

class Pracownik:

    def __init__(self, imie, wynagrodzenie_brutto):
        self.imie = imie
        self.wynagrodzenie_brutto = wynagrodzenie_brutto

    def pokaz_info_koncowe(self):
        print(self.imie
              + " "
              + str(f'{self.oblicz_wyplata_netto():.2f}')
              + " "
              + str(f'{self.oblicz_skladki():.2f}')
              + " "
              + str(f'{self.laczny_koszt_pracodawcy_na_pracownika():.2f}'))

    def oblicz_wyplata_netto(self):
        b = self.wynagrodzenie_brutto
        c = 0.0976 * b + 0.015 * b + 0.0245 * b
        r_c = round(c, 2)
        e = 0.09 * (b - r_c)
        r_e = round(e, 2)
        j = 0.18 * (b - 111.25 - c) - 0.0775 * (b - c)
        r_j = round(j, 2)
        wynagrodzenie_netto = b - r_c - r_e - r_j
        r_wynagrodzenie_netto = round(wynagrodzenie_netto, 2)
        return r_wynagrodzenie_netto

    def oblicz_skladki(self):
        brutto = self.wynagrodzenie_brutto
        r_brutto = round(brutto, 2)
        skladki = 0.0976 * r_brutto + 0.065 * r_brutto + 0.0193 * r_brutto + 0.0245 * r_brutto + 0.01 * r_brutto
        r_skladki = round(skladki, 2)
        return r_skladki

    def laczny_koszt_pracodawcy_na_pracownika(self):
        lacznykoszt = self.wynagrodzenie_brutto + self.oblicz_skladki()
        r_lacznykoszt = round(lacznykoszt,2 )
        return r_lacznykoszt


liczba_pracownikow = input()
n = int(liczba_pracownikow)
lista_pracownikow_razem = [input() for pracownik in range(n)]
splitter = []
liczLacznyKoszt = 0
for pracownikInput in lista_pracownikow_razem:
    splitter = pracownikInput.split()
    pracownik = Pracownik(imie=splitter[0], wynagrodzenie_brutto=float(splitter[1]))
    pracownik.pokaz_info_koncowe()
    liczLacznyKoszt += pracownik.laczny_koszt_pracodawcy_na_pracownika()

print(liczLacznyKoszt)
