import tkinter as tk
from tkinter import ttk, messagebox
import re
from datetime import datetime

class MikasStore:
    def __init__(self, master):
        self.master = master
        self.master.title("Mika's Store")
        self.master.geometry("600x400")
        
        self.usuarios = {}
        self.sesion_iniciada = None
        self.carrito_compra = []
        
        self.create_widgets()
        
    def create_widgets(self):
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill="both")
        
        self.main_frame = ttk.Frame(self.notebook)
        self.register_frame = ttk.Frame(self.notebook)
        self.login_frame = ttk.Frame(self.notebook)
        self.catalog_frame = ttk.Frame(self.notebook)
        self.invoice_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.main_frame, text="Inicio")
        self.notebook.add(self.register_frame, text="Registro")
        self.notebook.add(self.login_frame, text="Iniciar Sesión")
        self.notebook.add(self.catalog_frame, text="Catálogo")
        self.notebook.add(self.invoice_frame, text="Factura")
        
        self.setup_main_frame()
        self.setup_register_frame()
        self.setup_login_frame()
        self.setup_catalog_frame()
        self.setup_invoice_frame()
        
    def setup_main_frame(self):
        ttk.Label(self.main_frame, text="¡Bienvenido a Mika's Store!", font=("Arial", 16)).pack(pady=20)
        ttk.Label(self.main_frame, text="Conéctate con el futuro, elige tu próximo celular hoy", font=("Arial", 12)).pack()
        ttk.Label(self.main_frame, text="En Mika, encontrarás los mejores celulares y accesorios", font=("Arial", 10)).pack(pady=10)
        
    def setup_register_frame(self):
        ttk.Label(self.register_frame, text="Registro de Usuario", font=("Arial", 14)).pack(pady=10)
        
        ttk.Label(self.register_frame, text="Usuario:").pack()
        self.register_username = ttk.Entry(self.register_frame)
        self.register_username.pack()
        
        ttk.Label(self.register_frame, text="Contraseña:").pack()
        self.register_password = ttk.Entry(self.register_frame, show="*")
        self.register_password.pack()
        
        ttk.Button(self.register_frame, text="Registrar", command=self.registro_Usuario).pack(pady=10)
        
    def setup_login_frame(self):
        ttk.Label(self.login_frame, text="Iniciar Sesión", font=("Arial", 14)).pack(pady=10)
        
        ttk.Label(self.login_frame, text="Usuario:").pack()
        self.login_username = ttk.Entry(self.login_frame)
        self.login_username.pack()
        
        ttk.Label(self.login_frame, text="Contraseña:").pack()
        self.login_password = ttk.Entry(self.login_frame, show="*")
        self.login_password.pack()
        
        ttk.Button(self.login_frame, text="Iniciar Sesión", command=self.login).pack(pady=10)
        
    def setup_catalog_frame(self):
        ttk.Label(self.catalog_frame, text="Catálogo de Productos", font=("Arial", 14)).pack(pady=10)
        
        self.products = {
            1: {"nombre": "iPhone 16", "precio": 999.99},
            2: {"nombre": "Samsung Galaxy S23", "precio": 899.99},
            3: {"nombre": "Cargador Universal", "precio": 19.99},
            4: {"nombre": "Funda Protectora", "precio": 25.99},
        }
        
        for key, value in self.products.items():
            ttk.Label(self.catalog_frame, text=f"{key}. {value['nombre']} - ${value['precio']:.2f}").pack()
        
        ttk.Label(self.catalog_frame, text="Seleccione producto:").pack()
        self.product_var = tk.StringVar()
        self.product_entry = ttk.Entry(self.catalog_frame, textvariable=self.product_var)
        self.product_entry.pack()
        
        ttk.Label(self.catalog_frame, text="Cantidad:").pack()
        self.quantity_var = tk.StringVar()
        self.quantity_entry = ttk.Entry(self.catalog_frame, textvariable=self.quantity_var)
        self.quantity_entry.pack()
        
        ttk.Button(self.catalog_frame, text="Agregar al Carrito", command=self.add_to_cart).pack(pady=10)
        ttk.Button(self.catalog_frame, text="Finalizar Compra", command=self.finish_purchase).pack()
        
    def setup_invoice_frame(self):
        self.invoice_text = tk.Text(self.invoice_frame, height=20, width=70)
        self.invoice_text.pack(pady=10)
        
        ttk.Button(self.invoice_frame, text="Generar Factura", command=self.generate_invoice).pack()
        
    def registro_Usuario(self):
        usuario = self.register_username.get()
        contraseña = self.register_password.get()
        
        if usuario and contraseña:
            if usuario in self.usuarios:
                messagebox.showerror("Error", "El nombre de usuario ya está registrado.")
            else:
                self.usuarios[usuario] = {"contraseña": contraseña, "factura": None}
                messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
                self.register_username.delete(0, tk.END)
                self.register_password.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            
    def login(self):
        usuario = self.login_username.get()
        contraseña = self.login_password.get()
        
        if usuario in self.usuarios and self.usuarios[usuario]["contraseña"] == contraseña:
            self.sesion_iniciada = usuario
            messagebox.showinfo("Éxito", f"Bienvenido, {usuario}.")
            self.notebook.select(self.catalog_frame)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
            
    def add_to_cart(self):
        if not self.sesion_iniciada:
            messagebox.showerror("Error", "Debe iniciar sesión para realizar una compra.")
            return
        
        try:
            product_id = int(self.product_var.get())
            quantity = int(self.quantity_var.get())
            
            if product_id in self.products and quantity > 0:
                product = self.products[product_id]
                self.carrito_compra.append({
                    "producto": product["nombre"],
                    "precio": product["precio"],
                    "cantidad": quantity
                })
                messagebox.showinfo("Éxito", f"{quantity} {product['nombre']}(s) agregado(s) al carrito.")
                self.product_var.set("")
                self.quantity_var.set("")
            else:
                messagebox.showerror("Error", "Producto o cantidad inválida.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
            
    def finish_purchase(self):
        if not self.carrito_compra:
            messagebox.showinfo("Información", "El carrito está vacío.")
        else:
            self.notebook.select(self.invoice_frame)
            
    def generate_invoice(self):
        if not self.sesion_iniciada:
            messagebox.showerror("Error", "Debe iniciar sesión para generar una factura.")
            return
        
        if not self.carrito_compra:
            messagebox.showerror("Error", "El carrito está vacío.")
            return
        
        factura = self.usuarios[self.sesion_iniciada].get("factura", self.datos_ConsumidorFinal(None))
        
        hoy = datetime.now()
        fecha = hoy.strftime("%d/%m/%Y")
        hora = hoy.strftime("%H:%M:%S")
        
        invoice_content = f"""
{'='*61}
                    FACTURA DE COMPRA
{'='*61}
Tienda: Mika's Store
Dirección: Calle 123, Quito
Teléfono: +593 099 131 1404
Fecha de emisión: {fecha}    Hora: {hora}
{'-'*61}
Cliente: {factura['nombre']} - {factura['identificacion']}
Teléfono: {factura['telefono']}
Dirección: {factura['direccion']}
Correo: {factura['correo']}
{'-'*61}
{'Cantidad':<10}{'Descripción':<22}{'Precio Unitario':<21}{'Total':<12}
{'-'*61}
"""
        
        subtotal = 0
        for item in self.carrito_compra:
            total_producto = item["precio"] * item["cantidad"]
            subtotal += total_producto
            invoice_content += f"   {item['cantidad']:<7}{item['producto']:<25}${item['precio']:<17.2f}${total_producto:<9.2f}\n"
        
        impuestos = subtotal * 0.15
        total = subtotal + impuestos
        
        invoice_content += f"""
{'-'*61}
{'Subtotal':<35}${subtotal:.2f}
{'Impuestos (15%)':<35}${impuestos:.2f}
{'Total':<35}${total:.2f}
{'='*61}

                ¡Gracias por su compra!
"""
        
        self.invoice_text.delete(1.0, tk.END)
        self.invoice_text.insert(tk.END, invoice_content)
        
    def datos_ConsumidorFinal(self, datos_factura):
        if datos_factura is None:
            datos_factura = {}
        return {
            'nombre': datos_factura.get('nombre', 'Consumidor Final').upper(),
            'identificacion': datos_factura.get('identificacion', '9999999999'),
            'telefono': datos_factura.get('telefono', '0000000000'),
            'direccion': datos_factura.get('direccion', 'N/A').upper(),
            'correo': datos_factura.get('correo', 'N/A').upper()
        }

if __name__ == "__main__":
    root = tk.Tk()
    app = MikasStore(root)
    root.mainloop()
