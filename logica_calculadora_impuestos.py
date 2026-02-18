def calcular_impuestos(ingresos_anuales: float, deducciones: float, pension: float, salud: float, dependientes: int, vivienda_propia: bool) -> float:
    valor_uvt= 52374
    renta_pesos= renta_gravable(ingresos_anuales, deducciones, pension, salud)
    renta_uvt= renta_gravable_uvt(renta_pesos)

    if renta_uvt <= 1090:
        return 0
    elif renta_uvt <= 1_700:
        return ((renta_uvt - 1090) * 0.19) * valor_uvt
    elif renta_uvt <= 4_100:
        return (116 + (renta_uvt-1700)*0.28)* valor_uvt
    elif renta_uvt <= 8_670:
        return (788 + (renta_uvt-4100)*0.33)* valor_uvt
    elif renta_uvt <= 18_970:
        return (2296 + (renta_uvt-8670)*0.35) * valor_uvt
    elif renta_uvt <= 31_000:
        return (5901 + (renta_uvt-18970)*0.37)* valor_uvt
    else:
        return (10352 + (renta_uvt-31000)*0.39)* valor_uvt

def renta_gravable(ingresos_anuales: float, deducciones: float, pension: float, salud: float) -> float:
    #Calcular la renta gravable en pesos $
    return ingresos_anuales - (deducciones + pension + salud)

def renta_gravable_uvt(renta_gravable: float) -> float:
    #Pasar la renta gravable a UVT (2026)
    valor_uvt= 52374
    return renta_gravable / valor_uvt