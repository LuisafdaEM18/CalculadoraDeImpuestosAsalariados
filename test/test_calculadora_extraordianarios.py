import unittest
import sys
sys.path.append('src')

from model import logica_calculadora_impuestos



class TestCalculoImpuestosExtraordinarios(unittest.TestCase):
    def test_caso_extraordinario_ingresos_altos(self):
        ingresos_anuales = 600_000_000
        deducciones_generales = 60_000_000
        aporte_pension = 48_000_000
        aporte_salud = 24_000_000
        numero_dependientes = 4
        tiene_vivienda_propia = True
        intereses_credito_vivienda = 25_000_000
        impuesto_esperado = 107_835_039
        variables_impuestos= logica_calculadora_impuestos.VariablesImpuestos(ingresos_anuales, deducciones_generales,aporte_pension,aporte_salud,numero_dependientes,tiene_vivienda_propia,intereses_credito_vivienda )
        impuesto_calculado=logica_calculadora_impuestos.CalcularImpuesto.calcular_impuesto_renta(variables_impuestos)
        self.assertAlmostEqual(impuesto_calculado, impuesto_esperado)

    def test_caso_extraordinario_bajo_umbral(self):
        ingresos_anuales = 15_000_000
        deducciones_generales = 0
        aporte_pension = 1_200_000
        aporte_salud = 600_000
        numero_dependientes = 0
        tiene_vivienda_propia = False
        intereses_credito_vivienda = 0
        impuesto_esperado = 0
        variables_impuestos= logica_calculadora_impuestos.VariablesImpuestos(ingresos_anuales, deducciones_generales,aporte_pension,aporte_salud,numero_dependientes,tiene_vivienda_propia,intereses_credito_vivienda )
        impuesto_calculado=logica_calculadora_impuestos.CalcularImpuesto.calcular_impuesto_renta(variables_impuestos)
        self.assertAlmostEqual(impuesto_calculado, impuesto_esperado)

    def test_caso_extraordinario_maximo(self):
        ingresos_anuales = 1_200_000_000
        deducciones_generales = 0
        aporte_pension = 0
        aporte_salud = 0
        numero_dependientes = 0
        tiene_vivienda_propia = False
        intereses_credito_vivienda = 0
        impuesto_esperado = 362_700_849
        variables_impuestos= logica_calculadora_impuestos.VariablesImpuestos(ingresos_anuales, deducciones_generales,aporte_pension,aporte_salud,numero_dependientes,tiene_vivienda_propia,intereses_credito_vivienda )
        impuesto_calculado=logica_calculadora_impuestos.CalcularImpuesto.calcular_impuesto_renta(variables_impuestos)
        self.assertAlmostEqual(impuesto_calculado, impuesto_esperado)

if __name__ == '__main__':
    unittest.main()
        