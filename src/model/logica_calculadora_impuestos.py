class ErrorIngresos( Exception):
    """Los ingresos anuales deben ser mayor a cero"""
class ErrorTopesDeducciones(Exception):
    """Las deducciones no pueden ser mayores a los ingresos anuales"""
class ErrorDependientes(Exception):
    """Las deducciones deben ser mayores a cero"""
class ErrorPension(Exception):
    """La pensión debe ser mayor a cero"""
class ErrorInteresVivienda(Exception):
    """Los intereses de vivienda deben ser mayores a cero"""
    

def calcular_impuestos(ingresos_anuales: float, deducciones: float, pension: float, salud: float, dependientes: int, vivienda_propia: bool, intereses_vivienda: float = 0) -> float:
    # Validaciones
    if ingresos_anuales < 0:
        raise ErrorIngresos(f"ERROR: Los ingresos anuales no pueden ser negativos: {ingresos_anuales}$")
    if deducciones > ingresos_anuales:
        raise ErrorTopesDeducciones(f"ERROR: Las deducciones: {deducciones}$  no pueden superar los ingresos totales: {ingresos_anuales}$")
    if dependientes < 0:
        raise ErrorDependientes(f"ERROR: El número de dependientes: {dependientes} debe ser mayor o igual a cero")
    if pension < 0:
        raise ErrorPension(f"ERROR: Los aportes a pensión: {pension}$ no pueden ser negativos")
    if intereses_vivienda < 0:
        raise ErrorInteresVivienda(f"ERROR: Los intereses de vivienda: {intereses_vivienda}$ no pueden ser negativos")

    valor_uvt = 52374
    renta_pesos = renta_gravable(ingresos_anuales, deducciones, pension, salud, dependientes, vivienda_propia, intereses_vivienda)
    renta_uvt = renta_gravable_uvt(renta_pesos)

    if renta_uvt <= 1090:
        return 0
    elif renta_uvt <= 1700:
        return round(((renta_uvt - 1090) * 0.19) * valor_uvt, 0)
    elif renta_uvt <= 4100:
        return round((116 + (renta_uvt - 1700) * 0.28) * valor_uvt, 0)
    elif renta_uvt <= 8670:
        return round((788 + (renta_uvt - 4100) * 0.33) * valor_uvt, 0)
    elif renta_uvt <= 18970:
        return round((2296 + (renta_uvt - 8670) * 0.35) * valor_uvt, 0)
    elif renta_uvt <= 31000:
        return round((5901 + (renta_uvt - 18970) * 0.37) * valor_uvt, 0)
    else:
        return round((10352 + (renta_uvt - 31000) * 0.39) * valor_uvt, 0)


def renta_gravable(ingresos_anuales: float, deducciones: float, pension: float, salud: float, dependientes: int, vivienda_propia: bool, intereses_vivienda: float = 0) -> float:
    # Calcular la renta gravable en pesos $
    valor_uvt = 52374

    # Renta exenta: 25% de ingresos, máximo 790 UVT
    renta_exenta = min(ingresos_anuales * 0.25, 790 * valor_uvt)

    # Deducciones especiales con límite: 40% ingresos o 1,340 UVT (lo menor)
    deduccion_10_pct = min(ingresos_anuales * 0.1, 384 * valor_uvt)
    deduccion_dependientes = 72 * valor_uvt * min(dependientes, 4)
    deduccion_vivienda = min(intereses_vivienda, 1200 * valor_uvt) if vivienda_propia else 0
    deducciones_especiales = deducciones + deduccion_10_pct + deduccion_dependientes + deduccion_vivienda
    limite_deducciones = min(ingresos_anuales * 0.4, 1340 * valor_uvt)
    deducciones_especiales = min(deducciones_especiales, limite_deducciones)

    return max(0, ingresos_anuales - renta_exenta - (pension + salud) - deducciones_especiales)


def renta_gravable_uvt(renta_gravable: float) -> float:
    # Pasar la renta gravable a UVT (2026)
    valor_uvt = 52374
    return round(renta_gravable / valor_uvt, 2)