from Vagonas import vagonas
from Lokomotyvas import lokomotyvas


class traukinys:

    @property
    def traukinio_svoris(self):
        if not hasattr(self, '_traukinio_svoris'):
            self._traukinio_svoris = self.lmase
        return self._traukinio_svoris

    @traukinio_svoris.setter
    def traukinio_svoris(self, value):
        self._traukinio_svoris = value

    def __init__(self, traukinio_ID, lmase, lmax_mase, t_mase=None):
        self.traukinio_ID = traukinio_ID
        self.lok = lokomotyvas(lmase, lmax_mase)
        self.vagonai = {}
        if(t_mase is None):
            self.traukinio_mase = lmase
        else:
            self.traukinio_mase = t_mase

    def __add__(self, other):
        try:
            self.vagonai[other.vagono_ID] = other
            self.traukinio_mase += other.vagono_mase
        except:
            print("Error handled")
        return self

    def __sub__(self, other):
        try:
            self.traukinio_mase -= (other.vagono_mase + other.krovinio_mase)
            del self.vagonai[other.vagono_ID]
        except:
            print("Vagonas nerastas")
        return self

    def __repr__(self):
        return "'" + str(self) + "'"

    def __str__(self):
        return "Traukinio ID: " + str(self.traukinio_ID) \
               + "\nMaximali tempiamoji mase: "\
               + str(self.lok.max_tempiamoji_mase)\
               + "\nVagonu skaicius: " + str(len(self))\
               + "\nTraukinio mase: " + str(self.traukinio_mase)

    def __bool__(self):
        if(self.vagonai):
            return True
        else:
            return False

    def __len__(self):
        return len(self.vagonai)
