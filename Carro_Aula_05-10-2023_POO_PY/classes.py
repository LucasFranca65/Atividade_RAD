from email.errors import MalformedHeaderDefect


class Automoveis: ###Metodo Automoveis

    def __init__(self, marca, modelo , maxima, cor = "Branco"): ###Metododo construtor
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.veloAtual = 0
        self.veloMax = maxima
        self.ligado = False

    def acelerar(self, kmh): ###Metodo acelerar
        if(self.veloAtual + kmh) > self.veloMax:
            self.veloAtual = self.veloMax
        else:
            self.veloAtual += kmh
        
    def frear(self, kmh): ###Metodo Frear
        if(self.veloAtual - kmh) < 0:
            self.veloAtual = 0
        else:
            self.veloAtual -= kmh

    