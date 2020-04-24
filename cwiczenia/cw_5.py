#zadanie 1
class material
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
    def wyswietl_nazwe(self):
        print("To jest",self.rodzaj,"o dlugosci-",self.dlugosc,", i szerokosci-",self.szerokosc)

class ubrania(material):
    rozmiar="rozmiar"
    kolor="kolor"
    dla_kogo="dla kogo"
    def wyswietl_dane(self):
        print("rozmiar-",self.rozmiar,"kolor-",self.kolor,"dla kogo -",self.dla_kogo)

class sweter(ubrania):
    rodzaj_swetra="rodzaj np rozpinany"
    def wyswietl_dane_swetra(self):
        print("rodzaj swetra",self.rodzaj_swetra)