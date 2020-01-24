class Time:
    def __init__(self,czas):
        self.czas = czas

    def konwersja_na_minuty(self):
        minut = self.czas//60
        sekund = self.czas-(minut*60)
        return str(minut) + ":" + str(sekund)
    def konwersja_na_godziny(self):
        godzin = self.czas//3600
        minut = (self.czas-(godzin*3600))//60
        sekund = (self.czas-(godzin*3600)-(minut*60))
        return  str(godzin) + ":" + str(minut) + ":" + str(sekund)
