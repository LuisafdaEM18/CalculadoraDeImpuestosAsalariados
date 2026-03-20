
class ErrorIngresos(Exception):
    """Los ingresos anuales deben ser mayores o iguales a cero."""

class ErrorTopesDeducciones(Exception):
    """Las deducciones no pueden ser mayores a los ingresos anuales."""

class ErrorDependientes(Exception):
    """El número de dependientes debe ser mayor o igual a cero."""

class ErrorPension(Exception):
    """La pensión debe ser mayor o igual a cero."""

class ErrorInteresVivienda(Exception):
    """Los intereses de vivienda deben ser mayores o iguales a cero."""

class ErrorSalud(Exception):
    """La pensión debe ser mayor o igual a cero."""
    
class Variables_impuestos:
    def __init__(self,ingresos_anuales: float, deducciones: float, pension: float, salud: float, dependientes: int, tiene_vivienda_propia: int,intereses_vivienda: float):
        self.ingresos_anuales = ingresos_anuales
        self.deducciones = deducciones
        self.pension = pension
        self.salud = salud
        self.dependientes = dependientes
        self.tiene_vivienda_propia = tiene_vivienda_propia
        self.intereses_vivienda = intereses_vivienda

class Validar_variables:

    def validar_parametros_entrada(variables_impuestos) -> None:
        #Valida los parámetros de entrada para el cálculo de impuestos.
        if variables_impuestos.ingresos_anuales < 0:
            raise ErrorIngresos(f"ERROR: Los ingresos anuales no pueden ser negativos: {variables_impuestos.ingresos_anuales}$")
        if variables_impuestos.deducciones > variables_impuestos.ingresos_anuales:
            raise ErrorTopesDeducciones(f"ERROR: Las deducciones: {variables_impuestos.deducciones}$ no pueden superar los ingresos totales: {variables_impuestos.ingresos_anuales}$")
        if variables_impuestos.dependientes < 0:
            raise ErrorDependientes(f"ERROR: El número de dependientes: {variables_impuestos.dependientes} debe ser mayor o igual a cero")
        if variables_impuestos.pension < 0:
            raise ErrorPension(f"ERROR: Los aportes a pensión: {variables_impuestos.pension}$ no pueden ser negativos")
        if variables_impuestos.intereses_vivienda < 0:
            raise ErrorInteresVivienda(f"ERROR: Los intereses de vivienda: {variables_impuestos.intereses_vivienda}$ no pueden ser negativos")
        if variables_impuestos.salud < 0:
            raise ErrorSalud(f"ERROR: Aportes a salud: {variables_impuestos.salud}$ no pueden ser negativos")

class Calcular_impuesto:

    def calcular_impuesto_renta(variables_impuestos: Variables_impuestos) -> float:
        
        #Calcula el impuesto de renta a pagar según los parámetros de entrada.
        
        Validar_variables.validar_parametros_entrada(variables_impuestos)

        unidad_uvt = valor_uvt()
        base_gravable_pesos = calcular_base_gravable_pesos(variables_impuestos)
        base_gravable_uvt = convertir_pesos_a_uvt(base_gravable_pesos)

        if base_gravable_uvt <= 1090:
            return 0
        elif base_gravable_uvt <= 1700:
            return round(((base_gravable_uvt - 1090) * 0.19) * unidad_uvt, 0)
        elif base_gravable_uvt <= 4100:
            return round((116 + (base_gravable_uvt - 1700) * 0.28) * unidad_uvt, 0)
        elif base_gravable_uvt <= 8670:
            return round((788 + (base_gravable_uvt - 4100) * 0.33) * unidad_uvt, 0)
        elif base_gravable_uvt <= 18970:
            return round((2296 + (base_gravable_uvt - 8670) * 0.35) * unidad_uvt, 0)
        elif base_gravable_uvt <= 31000:
            return round((5901 + (base_gravable_uvt - 18970) * 0.37) * unidad_uvt, 0)
        else:
            return round((10352 + (base_gravable_uvt - 31000) * 0.39) * unidad_uvt, 0)

def valor_uvt():
    return 52374 #Valor actual en pesos de una UVT en 2026

def calcular_base_gravable_pesos(variables_impuestos: Variables_impuestos) -> float:
    unidad_uvt = valor_uvt()

    # Renta exenta: 25% de ingresos, máximo 790 UVT
    renta_exenta = min(variables_impuestos.ingresos_anuales * 0.25, 790 * unidad_uvt)

    # Deducciones especiales con límite: 40% ingresos o 1,340 UVT (lo menor)
    deduccion_10_por_ciento = min(variables_impuestos.ingresos_anuales * 0.1, 384 * unidad_uvt)
    deduccion_por_dependientes = 72 * unidad_uvt * min(variables_impuestos.dependientes, 4)
    deduccion_por_vivienda = min(variables_impuestos.intereses_vivienda, 1200 * unidad_uvt) if variables_impuestos.tiene_vivienda_propia else 0
    total_deducciones_especiales = variables_impuestos.deducciones + deduccion_10_por_ciento + deduccion_por_dependientes + deduccion_por_vivienda
    limite_deducciones_especiales = min(variables_impuestos.ingresos_anuales * 0.4, 1340 * unidad_uvt)
    total_deducciones_especiales = min(total_deducciones_especiales, limite_deducciones_especiales)

    return max(0, variables_impuestos.ingresos_anuales - renta_exenta - (variables_impuestos.aporte_pension + variables_impuestos.aporte_salud) - total_deducciones_especiales)



def convertir_pesos_a_uvt(base_gravable_pesos: float) -> float:
    unidad_uvt = valor_uvt()
    return round(base_gravable_pesos / unidad_uvt, 2)