class informacion:

    def mi_Lista(self):
        lista_Nomperros=["Boby", "Dollar", "Fany"]
        for x in lista_Nomperros:
            print(x)
    
    def mi_Tupla(self):
        Tupla_Edadperros=(15, 2, 18)
        for y in Tupla_Edadperros:
            print(y)

    def mi_Set(self):
        Set_Razaperros=("Chihuahua", "Salchicha", "Pastor Aleman")
        for z in Set_Razaperros:
            print(z)

    def mi_Diccionario(self):
        diccionariocolor = {
            "Negro": "Negro",
            "Verde": "Verde",
            "Cafe": "Cafe"
        }
        for x,y in diccionariocolor.items():
            print(x, y)
# Creando el objeto

Datos = informacion()
print("Listado de nombre de los perros")
Datos.mi_Lista()
print("Listado de edades de los perros")
Datos.mi_Tupla()
print("Listado de raza de los perros")
Datos.mi_Set()
print("Listado de colores de los perros")
Datos.mi_Diccionario()
