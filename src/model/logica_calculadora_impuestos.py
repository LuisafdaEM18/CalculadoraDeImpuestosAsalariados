
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
    


def validar_parametros_entrada(ingresos_anuales: float, deducciones: float, pension: float, salud: float, dependientes: int, intereses_vivienda: float) -> None:
    """Valida los parámetros de entrada para el cálculo de impuestos."""
    if ingresos_anuales < 0:
        raise ErrorIngresos(f"ERROR: Los ingresos anuales no pueden ser negativos: {ingresos_anuales}$")
    if deducciones > ingresos_anuales:
        raise ErrorTopesDeducciones(f"ERROR: Las deducciones: {deducciones}$ no pueden superar los ingresos totales: {ingresos_anuales}$")
    if dependientes < 0:
        raise ErrorDependientes(f"ERROR: El número de dependientes: {dependientes} debe ser mayor o igual a cero")
    if pension < 0:
        raise ErrorPension(f"ERROR: Los aportes a pensión: {pension}$ no pueden ser negativos")
    if intereses_vivienda < 0:
        raise ErrorInteresVivienda(f"ERROR: Los intereses de vivienda: {intereses_vivienda}$ no pueden ser negativos")


def calcular_impuesto_renta(ingresos_anuales: float, deducciones_generales: float, aporte_pension: float, aporte_salud: float, numero_dependientes: int, tiene_vivienda_propia: bool, intereses_credito_vivienda: float = 0) -> float:
    """
    Calcula el impuesto de renta a pagar según los parámetros de entrada.
    """
    validar_parametros_entrada(ingresos_anuales, deducciones_generales, aporte_pension, aporte_salud, numero_dependientes, intereses_credito_vivienda)

    valor_uvt = 52374
    base_gravable_pesos = calcular_base_gravable_pesos(
        ingresos_anuales,
        deducciones_generales,
        aporte_pension,
        aporte_salud,
        numero_dependientes,
        tiene_vivienda_propia,
        intereses_credito_vivienda
    )
    base_gravable_uvt = convertir_pesos_a_uvt(base_gravable_pesos)

    if base_gravable_uvt <= 1090:
        return 0
    elif base_gravable_uvt <= 1700:
        return round(((base_gravable_uvt - 1090) * 0.19) * valor_uvt, 0)
    elif base_gravable_uvt <= 4100:
        return round((116 + (base_gravable_uvt - 1700) * 0.28) * valor_uvt, 0)
    elif base_gravable_uvt <= 8670:
        return round((788 + (base_gravable_uvt - 4100) * 0.33) * valor_uvt, 0)
    elif base_gravable_uvt <= 18970:
        return round((2296 + (base_gravable_uvt - 8670) * 0.35) * valor_uvt, 0)
    elif base_gravable_uvt <= 31000:
        return round((5901 + (base_gravable_uvt - 18970) * 0.37) * valor_uvt, 0)
    else:
        return round((10352 + (base_gravable_uvt - 31000) * 0.39) * valor_uvt, 0)



def calcular_base_gravable_pesos(ingresos_anuales: float, deducciones_generales: float, aporte_pension: float, aporte_salud: float, numero_dependientes: int, tiene_vivienda_propia: bool, intereses_credito_vivienda: float = 0) -> float:
    """
    Calcula la base gravable en pesos a partir de los parámetros de entrada.
    """
    valor_uvt = 52374

    # Renta exenta: 25% de ingresos, máximo 790 UVT
    renta_exenta = min(ingresos_anuales * 0.25, 790 * valor_uvt)

    # Deducciones especiales con límite: 40% ingresos o 1,340 UVT (lo menor)
    deduccion_10_por_ciento = min(ingresos_anuales * 0.1, 384 * valor_uvt)
    deduccion_por_dependientes = 72 * valor_uvt * min(numero_dependientes, 4)
    deduccion_por_vivienda = min(intereses_credito_vivienda, 1200 * valor_uvt) if tiene_vivienda_propia else 0
    total_deducciones_especiales = deducciones_generales + deduccion_10_por_ciento + deduccion_por_dependientes + deduccion_por_vivienda
    limite_deducciones_especiales = min(ingresos_anuales * 0.4, 1340 * valor_uvt)
    total_deducciones_especiales = min(total_deducciones_especiales, limite_deducciones_especiales)

    return max(0, ingresos_anuales - renta_exenta - (aporte_pension + aporte_salud) - total_deducciones_especiales)



def convertir_pesos_a_uvt(base_gravable_pesos: float) -> float:
    """
    Convierte la base gravable en pesos a UVT (2026).
    """
    valor_uvt = 52374
    return round(base_gravable_pesos / valor_uvt, 2)