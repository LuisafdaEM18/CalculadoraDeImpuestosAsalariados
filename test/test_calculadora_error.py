import unittest

import sys
sys.path.append('src')

from model import logica_calculadora_impuestos



class TestErroresCalculoImpuestos(unittest.TestCase):
    def test_error_ingresos_negativos(self):
        ingresos_anuales = -50_000_000
        deducciones_generales = 5_000_000
        aporte_pension = 4_000_000
        aporte_salud = 2_000_000
        numero_dependientes = 1
        tiene_vivienda_propia = True
        intereses_credito_vivienda = 3_000_000
        variables_impuestos= logica_calculadora_impuestos.Variables_impuestos(ingresos_anuales, deducciones_generales,aporte_pension,aporte_salud,numero_dependientes,tiene_vivienda_propia,intereses_credito_vivienda )
        with self.assertRaises(logica_calculadora_impuestos.ErrorIngresos):
            logica_calculadora_impuestos.Calcular_impuesto.calcular_impuesto_renta(variables_impuestos)

    def test_error_deducciones_excesivas(self):
        ingresos_anuales = 50_000_000
        deducciones_generales = 60_000_000
        aporte_pension = 4_000_000
        aporte_salud = 2_000_000
        numero_dependientes = 1
        tiene_vivienda_propia = False
        intereses_credito_vivienda = 0
        variables_impuestos= logica_calculadora_impuestos.Variables_impuestos(ingresos_anuales, deducciones_generales,aporte_pension,aporte_salud,numero_dependientes,tiene_vivienda_propia,intereses_credito_vivienda )
        with self.assertRaises(logica_calculadora_impuestos.ErrorIngresos):
            logica_calculadora_impuestos.Calcular_impuesto.calcular_impuesto_renta(variables_impuestos)

    def test_error_dependientes_negativos(self):
        ingresos_anuales = 80_000_000
        deducciones_generales = 10_000_000
        aporte_pension = 6_400_000
        aporte_salud = 3_200_000
        numero_dependientes = -2
        tiene_vivienda_propia = True
        intereses_credito_vivienda = 5_000_000
        variables_impuestos= logica_calculadora_impuestos.Variables_impuestos(ingresos_anuales, deducciones_generales,aporte_pension,aporte_salud,numero_dependientes,tiene_vivienda_propia,intereses_credito_vivienda )
        with self.assertRaises(logica_calculadora_impuestos.ErrorIngresos):
            logica_calculadora_impuestos.Calcular_impuesto.calcular_impuesto_renta(variables_impuestos)

    def test_error_aporte_pension_negativo(self):
        ingresos_anuales = 100_000_000
        deducciones_generales = 15_000_000
        aporte_pension = -8_000_000
        aporte_salud = 4_000_000
        numero_dependientes = 2
        tiene_vivienda_propia = True
        intereses_credito_vivienda = 6_000_000
        variables_impuestos= logica_calculadora_impuestos.Variables_impuestos(ingresos_anuales, deducciones_generales,aporte_pension,aporte_salud,numero_dependientes,tiene_vivienda_propia,intereses_credito_vivienda )
        with self.assertRaises(logica_calculadora_impuestos.ErrorIngresos):
            logica_calculadora_impuestos.Calcular_impuesto.calcular_impuesto_renta(variables_impuestos)

    def test_error_intereses_vivienda_negativos(self):
        ingresos_anuales = 90_000_000
        deducciones_generales = 12_000_000
        aporte_pension = 7_200_000
        aporte_salud = 3_600_000
        numero_dependientes = 1
        tiene_vivienda_propia = True
        intereses_credito_vivienda = -3_000_000
        variables_impuestos= logica_calculadora_impuestos.Variables_impuestos(ingresos_anuales, deducciones_generales,aporte_pension,aporte_salud,numero_dependientes,tiene_vivienda_propia,intereses_credito_vivienda )
        with self.assertRaises(logica_calculadora_impuestos.ErrorIngresos):
            logica_calculadora_impuestos.Calcular_impuesto.calcular_impuesto_renta(variables_impuestos)

if __name__ == '__main__':
    unittest.main()