class Te:
    duracion = 365
    
    @staticmethod
    def tiempo_recomendacion(sabor:int):    
        if sabor == 1:
            return  'te negro', 3 , 'Consumir al desayuno' 
        elif sabor == 2:
            return 'te verde', 5 , 'Consumir al medio dia'
        else:
            return 'te de hierbas', 6, 'Consumir al atardecer'
        
    @staticmethod
    def obtener_precio(formato:int):
        return 3000 if formato == 30 else 5000