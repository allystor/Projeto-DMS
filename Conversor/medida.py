class Medida:
    def __init__(self,milhas,polegada,pe,quilometro,centimetros,metros):
        self.__milhas = milhas
        self.__polegada = polegada
        self.__pe = pe
        self.__quilometros = quilometro
        self.__centimetros = centimetros
        self.__metros = metros

#convertendo Milhas

    def get_milhas_in(self,milhas):
        self.__polegada =63360
        return self.__polegada * milhas
    def get_milhas_ft(self,milhas):
        self.__pe = 5280
        return self.__pe * milhas
    def get_milhas_km(self,milhas):
        self.__quilometros =1.6093
        return self.__quilometros * milhas
    def get_milhas_cm(self,milhas):
        self.__centimetros =160934.4
        return self.__centimetros * milhas
    def get_milhas_m(self,milhas):
        self.__metros =1609.34
        return self.__metros * milhas

#convertendo Polegadas

    def get_polegadas_mi(self,polegada):
        self.__milhas = 0.0000157828
        return self.__milhas * polegada
    def get_polegadas_ft(self,polegada):
        self.__pe = 0.083333
        return self.__pe * polegada
    def get_polegadas_km(self,polegada):
        self.__quilometros =0.0000254
        return self.__quilometros * polegada
    def get_polegadas_cm(self,polegada):
        self.__centimetros = 2.54
        return self.__centimetros * polegada
    def get_polegadas_m(self,polegada):
        self.__metros = 0.0254
        return self.__metros * polegada

#convertendo Pés

    def get_pe_mi(self,pe):
        self.__milhas = 0.00018939
        return self.__milhas * pe
    def get_pe_in(self,pe):
        self.__polegada = 12
        return self.__polegada * pe
    def get_pe_km(self,pe):
        self.__quilometros = 0.0003048
        return self.__quilometros * pe
    def get_pe_cm(self,pe):
        self.__centimetros = 30.48
        return self.__centimetros * pe
    def get_pe_m(self,pe):
        self.__metros = 0.3048
        return self.__metros * pe

#convertendo Quilometros

    def get_quilometros_mi(self,quilometros):
        self.__milhas = 0.621371
        return self.__milhas * quilometros
    def get_quilometros_ft(self,quilometros):
        self.__pe = 3280.84
        return self.__pe * quilometros
    def get_quilometros_in(self,quilometros):
        self.__polegada = 39370.08
        return self.__polegada * quilometros
    def get_quilometros_cm(self,quilometros):
        self.__centimetros = 100000
        return self.__centimetros * quilometros
    def get_quilometros_m(self,quilometros):
        self.__metros = 1000
        return self.__metros * quilometros

#convertendo centímetros

    def get_centimetros_mi(self,centimetros):
        self.__milhas = 0.0000062137
        return self.__milhas * centimetros
    def get_centimetros_ft(self,centimetros):
        self.__pe = 0.032808
        return self.__pe * centimetros
    def get_centimetros_in(self,centimetros):
        self.__polegada = 0.393701
        return self.__polegada * centimetros
    def get_centimetros_km(self,centimetros):
        self.__quilometros = 0.00001
        return self.__quilometros * centimetros
    def get_centimetros_m(self,centimetros):
        self.__metros = 0.01
        return self.__metros * centimetros

#convertendo Metros

    def get_metros_mi(self,metros):
        self.__milhas = 0.00062137
        return self.__milhas * metros
    def get_metros_ft(self,metros):
        self.__pe = 3.2808
        return self.__pe * metros
    def get_metros_in(self,metros):
        self.__polegada = 39.3701
        return self.__polegada * metros
    def get_metros_km(self,metros):
        self.__quilometros = 0.001
        return self.__quilometros * metros
    def get_metros_cm(self,metros):
        self.__centimetros = 100
        return self.__centimetros * metros
