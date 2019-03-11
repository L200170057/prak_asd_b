''' Nama  : Titis Ulfa Mustikawati
    NIM   : L200170057
    Kelas : B
    Modul : 2 '''

class Pesan(object):

    #a
    def __init__(self, kata):
        self.kata = kata

    def apakahTerkandung(self, yo):
        if yo in self.kata:
            return True
        else:
            return False

    #b
    def hitungKonsonan(self):
        vokal = 'AIUEOaiueo'
        v = 0
        for x in self.kata:
            if x in vokal:
                v+=1
        kon = len(self.kata) - v
        return kon

    #c 
    def hitungVokal(self):
        vokal = 'AIUEOaiueo'
        v = 0
        for x in self.kata:
            if x in vokal:
                v+=1
        return v
