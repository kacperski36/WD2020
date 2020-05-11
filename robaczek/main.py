import random
class obiekt:
    def __init__(self,x,y):
       self.x=x
       self.y=y

class owoc(obiekt):
    jedzenie=random.randint(1,5)

class robaczek(obiekt):
    predkosc=1
    poziom=0
    najedzenie=0
    def zjedzOwoc(self,owoc):
        self.najedzenie+=owoc.jedzenie
    def sprawdz_poziom(self):
        if self.najedzenie%5==0:
            self.poziom+=1
            self.najedzenie-=5

def czy_zje(owoc,robaczek):
    if owoc.x==robaczek.x and owoc.y==robaczek.y:
        return True
