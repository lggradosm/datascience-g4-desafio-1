from tkinter.ttk import Treeview
from tkinter import *
from tkinter import messagebox

class Empresa: 
    
    def __init__(self, app):
        self.app = app
        self.app.title("Crud de empresas")
        self.app.geometry("640x480")

        frame = LabelFrame(self.app, text = "Nueva empresa")
        frame.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        lb_ruc = Label(frame, text="RUC")
        lb_ruc.grid(row=1, column=0)
        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row=1,column=1)


        lb_razon_social = Label(frame, text="Razon social")
        lb_razon_social.grid(row=2, column=0)
        self.txt_razon_social = Entry(frame)
        self.txt_razon_social.grid(row=2,column=1)

        lb_direccion = Label(frame, text="Direccion")
        lb_direccion.grid(row=3, column=0)
        self.txt_direccion = Entry(frame)
        self.txt_direccion.grid(row=3,column=1)

        btn_insertar = Button(frame, text="Nueva empresa",command=self.insertar)
        btn_insertar.grid(row=4,column=1)

        btn_insertar = Button(frame, text="Actualizar empresa",command=self.actualizar)
        btn_insertar.grid(row=4,column=2)

        btn_eliminar = Button(frame, text="Eliminar empresa", command=self.eliminar)
        btn_eliminar.grid(row=4, column=3 )

        self.tree = Treeview(self.app)
        self.tree['columns'] = ("RUC", "Razon social", "Direccion")

        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("RUC")
        self.tree.column("Razon social")
        self.tree.column("Direccion")

        self.tree.heading("#0", text="id")
        self.tree.heading("RUC")
        self.tree.heading("Razon social")
        self.tree.heading("Direccion")

        self.tree.grid(row=5,column=0,padx=20,pady=20)



    def insertar(self):
        nueva_empresa = (self.txt_ruc.get(), self.txt_razon_social.get(), self.txt_direccion.get())
        self.tree.insert("",END,values=nueva_empresa)
        self.limpiar()

    def eliminar(self):
        selection = self.tree.selection()
        if selection:
            for item in selection:
                self.tree.delete(item)
        else:
            messagebox.showerror("Alerta","Por favor seleccione un registro")

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

    def limpiar(self):
        self.txt_ruc.delete(0,END)
        self.txt_razon_social.delete(0, END)
        self.txt_direccion.delete(0,END)


