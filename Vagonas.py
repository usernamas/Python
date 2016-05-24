class vagonas:

    '''
Vagonas turi ID, mase, max krovinio mase ir krovinio mase.

Pridedant kroviny prie vagono tikrinama ar mase nevirsys maximalio vagono
krovinio mases.

Atemant kroviny is vagono tikrinama ar atemama mase nera didesne uz pati
krovini, kad nebutu taip jog vagono mase taptu neigiama.
    '''

    def __init__(self, vagono_ID, vagono_mase, max_krovinio_mase, z=0):
        self.vagono_ID = vagono_ID
        self.vagono_mase = vagono_mase
        self.max_krovinio_mase = max_krovinio_mase
        self.krovinio_mase = z

    def __add__(self, other):
        if((self.krovinio_mase + other) <= self.max_krovinio_mase):
            try:
                self.krovinio_mase += other
            except:
                print("Error")
        else:
            print("Krovinys per sunkus")
        return self

    def __sub__(self, other):
        if(self.krovinio_mase >= other):
            try:
                self.krovinio_mase -= other
            except:
                print("Error")
        else:
            print("Krovinio mase per didele, iveskite mazesne mase")
        return self
