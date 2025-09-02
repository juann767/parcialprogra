class Aparato:
    def __init__(self, nombre, potencia, horas):
        """
        Inicializa un aparato eléctrico
        :param nombre: Nombre del aparato
        :param potencia: Potencia en watts (W)
        :param horas: Horas de uso al mes
        """
        self.nombre = nombre
        self.potencia = potencia
        self.horas = horas

    def consumo_kwh(self):
        """
        Calcula el consumo mensual en kWh
        Fórmula: (potencia (W) * horas) / 1000
        """
        return (self.potencia * self.horas) / 1000

    def costo(self, tarifa):
        """
        Calcula el costo en base a la tarifa $/kWh
        """
        return self.consumo_kwh() * tarifa
