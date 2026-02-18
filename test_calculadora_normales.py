import logica_calculadora_impuestos
import unittest

class TestCalculadoraImpuesto(unittest.TestCase):

    def test_normal_1(self):
        #Entradas
        ingresos_anuales= 80_000_000
        deducciones= 10_000_000
        pension= 6_400_000
        salud= 3_200_000
        dependientes= 2
        vivienda_propia= True # 1 es SI y 2 es NO
        #Proceso
        impuesto_calculado= logica_calculadora_impuestos.calcular_impuestos(ingresos_anuales, deducciones, pension, salud, dependientes, vivienda_propia)
        #Salida
        impuesto_esperado= 629_344.6
        self.assertAlmostEqual(impuesto_calculado, impuesto_esperado, 2)

    def test_normal_2(self):
        #Entradas
        ingresos_anuales= 150_000_000
        deducciones= 20_000_000
        pension= 12_000_000
        salud= 6_000_000
        dependientes= 1
        vivienda_propia= False # 1 es SI y 2 es NO
        #Proceso
        impuesto_calculado= logica_calculadora_impuestos.calcular_impuestos(ingresos_anuales, deducciones, pension, salud, dependientes, vivienda_propia)
        #Salida
        impuesto_esperado= 12_500_122.6
        self.assertAlmostEqual(impuesto_calculado, impuesto_esperado, 2)
    
if __name__ == 'main':
    unittest.main()