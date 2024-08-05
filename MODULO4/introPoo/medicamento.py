class Medicamento():
    nombre = ""
    precio = 0
    descuento = 0.05
    IVA = 0.18
    def definicion(self):
        return f"{self.nombre} | ${self.precio}"
    
    @staticmethod
    def definicion2():
        return f"{Medicamento.nombre} | ${Medicamento.precio}"
    
    @staticmethod
    def validar_mayor_a_cero(numero:int):
        return numero > 0       
    
if __name__ == "__main__":
    m1 = Medicamento()
    m1.nombre = "Paracetamol"
    m1.precio = 2000
    print(m1.nombre)