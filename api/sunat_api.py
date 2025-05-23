import requests
from model.empresa import Empresa
class SunatAPi:

    TOKEN = "710ea44b1087d194503ba3b5857dda760a37cdfde85c13d3448b5cd6db462f23"
    API_URL = "https://apiperu.dev/api/ruc"
    
    def __init__(self):
        pass

    def obtener_empresa(self, ruc):
        OK = 200
        try:
            
            data_request = {
                "ruc": ruc
            }

            headers = {
                "Authorization": f"Bearer {self.TOKEN}",
                "Content-Type": "application/json"
            }
            response = requests.post(self.API_URL, json=data_request, headers=headers)

            if response.status_code == OK:
                data = response.json()["data"]
                empresa = Empresa(ruc=data["ruc"], razon_social=data["nombre_o_razon_social"], direccion=data["direccion"])
                return empresa
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    