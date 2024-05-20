class Boligrafo:
    def __init__(self, color, grosor):
        self.capacidad_tinta_maxima = 100
        self.cantidad_tinta = 80
        self.color = color
        self.grosor_punta = grosor
        self.colores = ["azul", "rojo"]
        self.grosores = ["fino", "grueso"]



    def escribir_texto(self, texto,color, grosor):
        caracter = len(texto)
        if self.grosor_punta == "fino":
            gasto_tinta = caracter
        elif self.grosor_punta == "grueso":
            gasto_tinta = caracter * 2
        elif self.grosor_punta == "extrafino":
            gasto_tinta = caracter * 0.5
        elif self.grosor_punta == "extragrueso":
            gasto_tinta = caracter * 4
        else:
            return "Grosor de punta y/o color no válido"

        if gasto_tinta > self.cantidad_tinta:
            return "No alcanza la tinta"
        else:
            self.cantidad_tinta -= gasto_tinta
            return f"Su texto es: {texto}, su texto lo ha dejado con {self.cantidad_tinta} de tinta en total"

    def recargar(self, cantidad):
        if self.cantidad_tinta + cantidad > self.capacidad_tinta_maxima:
            sobrante = (self.cantidad_tinta + cantidad) - self.capacidad_tinta_maxima
            self.cantidad_tinta = self.capacidad_tinta_maxima
            return f"Se recargó el bolígrafo y sobró {sobrante} cantidad de tinta"
        else:
            self.cantidad_tinta += cantidad
            if self.cantidad_tinta == self.capacidad_tinta_maxima:
                return "Bolígrafo recargado al 100%"
            else:
                return f"Su bolígrafo ahora tiene {self.cantidad_tinta} de tinta"
    
    def seleccionar_color(boligrafo):
        print("Colores instalados:")
        for i, color in enumerate(boligrafo.colores[:5], 1):
            print(f"{i}. {color}")
        color_texto = input("Seleccione el color con el que desea escribir el texto: ").lower()
        while color_texto not in boligrafo.colores:
            print("Color no válido. Por favor, seleccione un color instalado.")
            color_texto = input("Seleccione el color con el que desea escribir el texto: ").lower()
        return color_texto

    def seleccionar_grosor(boligrafo):
        print("Grosores instalados:")
        for i, grosor in enumerate(boligrafo.grosores[:5], 1):
            print(f"{i}. {grosor}")
        grosor_texto = input("Seleccione el grosor con el que desea escribir el texto: ").lower()
        while grosor_texto not in boligrafo.grosores:
            print("Grosor no válido. Por favor, seleccione un grosor instalado.")
            grosor_texto = input("Seleccione el grosor con el que desea escribir el texto: ").lower()
        return grosor_texto

    def agregar_color(self):
        while True:
            color = input("¿Qué color desea instalar? (Escriba 'No' para omitir): ")
            if color.lower() == "no":
                return "Omitiendo agregar color..."
            elif color in self.colores:
                return f"El color {color} ya está instalado"
            else:
                self.colores.append(color)
                return f"El color {color} ha sido instalado"

    def eliminar_color(self):
        while True:
            color = input(f"¿Qué color desea desinstalar? {self.colores} (Escriba 'No' para omitir): ")
            if color.lower() == "no":
                return "Omitiendo eliminar color..."
            elif color in self.colores:
                self.colores.remove(color)
                return f"El color {color} ya no está instalado"
            else:
                return f"El color {color} no está en la lista de colores instalados"

    def agregar_grosor(self):
        while True:
            grosor = input("¿Qué grosor desea agregar de los posibles (extragrueso o extrafino)? (Escriba 'No' para omitir): ")
            if grosor.lower() == "no":
                return "Omitiendo agregar grosor..."
            elif grosor.replace(" ", "").lower() not in ["extrafino", "extragrueso"]:
                print("Por favor, seleccione 'extrafino' o 'extragrueso'.")
            else:
                self.grosor_punta = grosor
                self.grosores.append(grosor)
                return f"El grosor {grosor} se ha instalado exitosamente"
        
    def eliminar_grosor(self):
        while True:
            grosor = input(f"¿Qué grosor desea desinstalar? {self.grosores} (Escriba 'No' para omitir): ")
            if grosor.lower() == "no":
                return "Omitiendo eliminar grosor..."
            elif grosor in self.grosores:
                self.grosores.remove(grosor)
                return f"El grosor {grosor} ya no está instalado"
            else:
                return f"El grosor {grosor} no está en la lista de grosores instalados"
    
    def mostrar_colores_instalados(self):
        self.colores.sort()  
        print("Colores instalados:")
        for i, color in enumerate(self.colores, 1):
            print(f"{i}. {color}")

    def mostrar_grosores_instalados(self):
        self.grosores.sort()
        print("Grosores Instalados: ")
        for i, grosor in enumerate(self.grosores, 1):
            print(f"{i}. {grosor}")