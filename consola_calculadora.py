import logica_calculadora_impuestos

def main():
    print("Bienvenido al programa que le ayuda a calcular la cantidad de impuestos a pagar")
    try:
        ingresos_anuales = float(input("Ingresos anuales: "))
        deducciones = float(input("Deducciones: "))
        pension = float(input("Aportes a la pensión: "))
        salud = float(input("Aportes a salud: "))
        dependientes = int(input("Dependientes: "))
        print("Elija la opción:")
        print("1. Sí tiene vivienda propia")
        print("2. No tiene vivienda propia")
        opcion_vivienda = int(input("Opción (1/2): "))
        vivienda_propia = True if opcion_vivienda == 1 else False
        intereses_vivienda = float(input("Intereses de la vivienda: "))

        impuesto = logica_calculadora_impuestos.calcular_impuestos(
            ingresos_anuales,
            deducciones,
            pension,
            salud,
            dependientes,
            vivienda_propia
        )
        print(f"\nEl impuesto a pagar es: ${impuesto:,.2f}")
    except Exception as err:
        print("No se pudo calcular. ", err)

if __name__ == "__main__":
    main()