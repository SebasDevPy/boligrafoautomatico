from class_boligrafo import Boligrafo

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar color")
    print("2. Eliminar color")
    print("3. Agregar grosor")
    print("4. Eliminar grosor")
    print("5. Escribir texto")
    print("6. Mostrar cantidad de tinta")
    print("7. Recargar bolígrafo")
    print("8. Colores instalados")
    print("9. Grosores instalados")
    print("10. Salir ")

def main():
    color_inicial = input("Seleccione el color inicial entre 'azul' y 'rojo': ").lower()
    while color_inicial not in ['azul', 'rojo']:
        print("Color no válido. Por favor, seleccione 'azul' o 'rojo'.")
        color_inicial = input("Seleccione el color inicial entre 'azul' y 'rojo': ").lower()

    grosor_inicial = input("Seleccione el grosor inicial entre 'fino' y 'grueso': ")
    while grosor_inicial not in ["fino", "grueso"]:
        print("El grosor seleccionado no es válido, seleccione entre 'fino' y 'grueso'")
        grosor_inicial = input("Seleccione el grosor inicial entre 'fino' y 'grueso': ")

    boligrafo = Boligrafo(color_inicial, grosor_inicial)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(boligrafo.agregar_color())
        elif opcion == "2":
            print(boligrafo.eliminar_color())
        elif opcion == "3":
            print(boligrafo.agregar_grosor())
        elif opcion == "4":
            print(boligrafo.eliminar_grosor())
        elif opcion == "5":
            color_texto = boligrafo.seleccionar_color()
            grosor_texto = boligrafo.seleccionar_grosor()
            texto = input("Introduce el texto que quieres escribir: ")
            print(boligrafo.escribir_texto(texto, color_texto, grosor_texto))
        elif opcion == "6":
            print(f"Su bolígrafo tiene {boligrafo.cantidad_tinta} de tinta.")
        elif opcion == "7":
            cantidad_recarga = int(input("Introduce la cantidad de tinta para recargar: "))
            print(boligrafo.recargar(cantidad_recarga))
        elif opcion == "8":
            boligrafo.mostrar_colores_instalados()
        elif opcion == "9":
            boligrafo.mostrar_grosores_instalados()
        elif opcion == "10":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()