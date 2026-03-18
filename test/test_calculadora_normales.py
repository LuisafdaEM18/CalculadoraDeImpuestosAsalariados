import unittest
import sys
sys.path.append('src')

from model import logica_calculadora_impuestos


class TestCalculoImpuestosNormales(unittest.TestCase):
    def test_caso_normal_1(self):
        ingresos_anuales = 80_000_000
        deducciones_generales = 10_000_000
        aporte_pension = 6_400_000
        aporte_salud = 3_200_000
        numero_dependientes = 2
        tiene_vivienda_propia = True
        intereses_credito_vivienda = 5_000_000
        impuesto_esperado = 0
        variables_impuestos= logica_calculadora_impuestos.Variables_impuestos(ingresos_anuales, deducciones_generales,aporte_pension,aporte_salud,numero_dependientes,tiene_vivienda_propia,intereses_credito_vivienda )
        impuesto_calculado=logica_calculadora_impuestos.Calcular_impuesto.calcular_impuesto_renta(variables_impuestos)
        self.assertAlmostEqual(impuesto_calculado, impuesto_esperado)

    def test_caso_normal_2(self):
        ingresos_anuales = 150_000_000
        deducciones_generales = 20_000_000
        aporte_pension = 12_000_000
        aporte_salud = 6_000_000
        numero_dependientes = 1
        tiene_vivienda_propia = False
        intereses_credito_vivienda = 0
        impuesto_esperado = 0
        variables_impuestos= logica_calculadora_impuestos.Variables_impuestos(ingresos_anuales, deducciones_generales,aporte_pension,aporte_salud,numero_dependientes,tiene_vivienda_propia,intereses_credito_vivienda )
        impuesto_calculado=logica_calculadora_impuestos.Calcular_impuesto.calcular_impuesto_renta(variables_impuestos)
        self.assertAlmostEqual(impuesto_calculado, impuesto_esperado)

    def test_caso_normal_3(self):
        ingresos_anuales = 200_000_000
        deducciones_generales = 15_000_000
        aporte_pension = 10_000_000
        aporte_salud = 5_000_000
        numero_dependientes = 0
        tiene_vivienda_propia = True
        intereses_credito_vivienda = 2_000_000
        impuesto_esperado = 11_000_237
        variables_impuestos= logica_calculadora_impuestos.Variables_impuestos(ingresos_anuales, deducciones_generales,aporte_pension,aporte_salud,numero_dependientes,tiene_vivienda_propia,intereses_credito_vivienda )
        impuesto_calculado=logica_calculadora_impuestos.Calcular_impuesto.calcular_impuesto_renta(variables_impuestos)
        self.assertAlmostEqual(impuesto_calculado, impuesto_esperado)

if __name__ == '__main__':
    unittest.main()