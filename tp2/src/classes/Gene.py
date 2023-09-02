class Gene:

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

    @staticmethod
    def from_array(arr):
        return Gene(*arr)

    def to_array(self):
        return [self.fuerza, self.agilidad, self.pericia, self.resistencia, self.vida, self.altura]

    def __str__(self):
        return f'Gene(fuerza={self.fuerza}, agilidad={self.agilidad}, pericia={self.pericia}, resistencia={self.resistencia}, vida={self.vida}, altura={self.altura})'

    def __eq__(self, other):
        if not isinstance(other, Gene):
            return NotImplemented

        return (self.fuerza == other.fuerza) and (self.altura == other.altura) \
               and (self.vida == other.vida) and (self.resistencia == other.resistencia) \
               and (self.agilidad == other.agilidad) and (self.pericia == other.pericia)
