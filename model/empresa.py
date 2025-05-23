class Empresa: 
    
    def __init__(self, ruc, razon_social, direccion, id = None):
        self.id = id
        self.ruc = ruc
        self.razon_social = razon_social
        self.direccion = direccion
    