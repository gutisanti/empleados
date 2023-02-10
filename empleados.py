from datetime import datetime, date



class Empleado:

    def __init__(self, nombre: str, identificacion: str, fecha_nacimiento: date, fecha_ingreso: date, salario: float):
        self.nombre: str = nombre
        self.identifiacion: str = identificacion
        self.fecha_nacimiento: date = fecha_nacimiento
        self.fecha_ingreso: date = fecha_ingreso
        self.salario: float = salario

    def calcular_antiguedad(self) -> float
        date_diff = datetime.date(datetime.now()) - self.fecha_ingreso
        return (date_diff.day + date_diff.seconds / 86400) / 365