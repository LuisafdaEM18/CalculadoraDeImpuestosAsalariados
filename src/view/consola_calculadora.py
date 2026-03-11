import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from model import logica_calculadora_impuestos


def solicitar_datos_usuario():
    """Solicita y retorna los datos necesarios para el cálculo de impuestos."""
    print("Bienvenido al programa que le ayuda a calcular la cantidad de impuestos a pagar")
    ingresos_anuales = float(input("Ingresos anuales: "))
    deducciones_generales = float(input("Deducciones generales: "))
    aporte_pension = float(input("Aportes a la pensión: "))
    aporte_salud = float(input("Aportes a salud: "))
    numero_dependientes = int(input("Número de dependientes: "))
    print("Elija la opción:")
    print("1. Sí tiene vivienda propia")
    print("2. No tiene vivienda propia")
    opcion_vivienda = int(input("Opción (1/2): "))
    tiene_vivienda_propia = opcion_vivienda == 1
    intereses_credito_vivienda = float(input("Intereses de la vivienda: "))
    return (ingresos_anuales, deducciones_generales, aporte_pension, aporte_salud, numero_dependientes, tiene_vivienda_propia, intereses_credito_vivienda)

def mostrar_resultado(impuesto_calculado: float):
    """Muestra el resultado del cálculo de impuestos."""
    print(f"\nEl impuesto a pagar es: ${impuesto_calculado:,.2f}")

def main():
    try:
        datos = solicitar_datos_usuario()
        impuesto = logica_calculadora_impuestos.calcular_impuesto_renta(*datos)
        mostrar_resultado(impuesto)
    except Exception as error:
        print("No se pudo calcular. ", error)

if __name__ == "__main__":
    main()