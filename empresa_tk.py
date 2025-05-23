from tkinter.ttk import Treeview
from tkinter import *
from tkinter import messagebox
from api.sunat_api import SunatAPi
from dao.empresa_dao import EmpresaDAO
from model.empresa import Empresa
class EmpresaTK: 

    sunat_api =  SunatAPi()
    empresa_dao = EmpresaDAO()

    def __init__(self, app):
        self.app = app
        self.app.title("Crud de empresas")
        self.app.geometry("840x480")

        frame = LabelFrame(self.app, text = "Nueva empresa")
        frame.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        lb_ruc = Label(frame, text="RUC")
        lb_ruc.grid(row=1, column=0)
        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row=1,column=1)
        btn_buscar = Button(frame, text="Buscar",command=self.obtener_empresa)
        btn_buscar.grid(row=1,column=2, columnspan=2, padx=10)
        btn_buscar.config(width=13)

        lb_razon_social = Label(frame, text="Razon social")
        lb_razon_social.grid(row=2, column=0)
        self.txt_razon_social = Entry(frame)
        self.txt_razon_social.grid(row=2,column=1)
        self.txt_razon_social.config(state="disabled")

        lb_direccion = Label(frame, text="Direccion")
        lb_direccion.grid(row=3, column=0)
        self.txt_direccion = Entry(frame)
        self.txt_direccion.grid(row=3,column=1)
        self.txt_direccion.config(state="disabled")


        btn_insertar = Button(frame, text="Nueva empresa",command=self.insertar)
        btn_insertar.grid(row=4,column=1)


        btn_eliminar = Button(frame, text="Eliminar empresa", command=self.eliminar)
        btn_eliminar.grid(row=4, column=2, padx=10 )

        self.tree = Treeview(self.app)
        self.tree['columns'] = ("ID","RUC", "Razon social", "Direccion")

        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("ID")
        self.tree.column("RUC")
        self.tree.column("Razon social")
        self.tree.column("Direccion")

        self.tree.grid(row=5,column=0,padx=20,pady=20)
        self.imprimir_tabla()



    def insertar(self):
        try:
            nueva_empresa = Empresa(ruc=self.txt_ruc.get(), razon_social=self.txt_razon_social.get(), direccion=self.txt_direccion.get())
            result = self.empresa_dao.insert(nueva_empresa)
            if result == False:
                messagebox.showerror("Alerta","No se pudo crear el registro")
            self.imprimir_tabla()
            self.limpiar()
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Alerta","No se pudo crear el registro")

    def eliminar(self):
        try:
            selection = self.tree.selection()
            if selection:
                for item in selection:
                    valores = self.tree.item(item, 'values')
                    id = valores[0] 
                    result = self.empresa_dao.delete(id)
                    if result == True:
                        self.imprimir_tabla()
                    else: 
                        messagebox.showerror("Alerta","No se pudo eliminar el registro")
            else:
                messagebox.showerror("Alerta","Por favor seleccione un registro")
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Alerta","No se pudo eliminar el registro")

    def actualizar(self):
        selection = self.tree.selection()
        if selection:
            for item_id in selection:
                item = self.tree.item(item_id)
                values = item["values"]
                self.txt_ruc.insert(0, values[0])
                self.txt_razon_social.insert(0, values[1])
                self.txt_direccion.insert(0, values[2])
                
        else:
            messagebox.showerror("Alerta","Por favor seleccione un registro")

    def imprimir_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        data = self.empresa_dao.get_all()
        self.tree.heading("ID", text="ID")
        self.tree.heading("RUC", text="RUC")
        self.tree.heading("Razon social", text="Razón Social")
        self.tree.heading("Direccion", text="Dirección")
        for empresa in data:
            self.tree.insert("",END,values=empresa)

    def limpiar(self):
        self.txt_razon_social.config(state="normal")
        self.txt_direccion.config(state="normal")
        self.txt_ruc.delete(0,END)
        self.txt_razon_social.delete(0, END)
        self.txt_direccion.delete(0,END)
        self.txt_razon_social.config(state="disabled")
        self.txt_direccion.config(state="disabled")


    def obtener_empresa(self):
        ruc = self.txt_ruc.get()
        
        empresa = self.sunat_api.obtener_empresa(ruc)
        if empresa is not None:
            self.txt_razon_social.config(state="normal")
            self.txt_razon_social.delete(0, "end")
            self.txt_razon_social.insert(0, empresa.razon_social)
            self.txt_direccion.config(state="normal")
            self.txt_direccion.delete(0, "end")
            self.txt_direccion.insert(0, empresa.direccion)
            self.txt_razon_social.config(state="disabled")
            self.txt_direccion.config(state="disabled")
        else:
            messagebox.showerror("Alerta","No se pudo obtener la empresa")



