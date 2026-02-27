import logica_calculadora_impuestos
"Interfaz de usuario para la calculadora de impuestos" 

try:
    print("Bienvenido al programa que le ayuda a calcular la cantidad de impuestos a pagar")
    ingresos_anuales= float(input("Ingresos anuales: "))
    deducciones= float(input("Deducciones: "))
    aportes_pension= float(input("Aportes a la pensión: "))
    dependientes= int(input("Dependientes: "))
    print("Elija la opcion")
    print("1. Si tiene vivienda propia")
    print("2. Si no tiene vivienda propia")
    vivienda_propia= int(input("Opcion: ")) 
    renta_liquida_gravable= float(input("Renta liquida : "))
    
except Exception as err: 
    print("No se pudo calcular")
    print()