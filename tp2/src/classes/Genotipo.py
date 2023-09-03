class Genotipo:

    def __init__(self, fuerza, agilidad, pericia, resistencia, vida, altura):
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.pericia = pericia
        self.resistencia = resistencia
        self.vida = vida
        self.altura = altura

    def get_fuerza(self):
        return self.fuerza

    def get_agilidad(self):
        return self.agilidad

    def get_pericia(self):
        return self.pericia

    def get_resistencia(self):
        return self.resistencia

    def get_vida(self):
        return self.vida

    def get_altura(self):
        return self.altura

    def set_agilidad(self, agilidad):
        self.agilidad = agilidad

    def set_fuerza(self, fuerza):
        self.fuerza = fuerza

    def set_pericia(self, pericia):
        self.pericia = pericia

    def set_resistencia(self, resistencia):
        self.resistencia = resistencia

    def set_vida(self, vida):
        self.vida = vida

    def set_altura(self, altura):
        self.altura = altura
