import logica_calculadora_impuestos
import unittest

class TestCalculadoraImpuesto(unittest.TestCase):

    def test_normal_1(self):
        
        #Entradas

        ingresos_anuales= 80000000
        deducciones= 10000000
        pension= 6400000
        salud= 3200000
        dependientes= 2
        vivienda_propia= 1 # 1 es SI y 2 es NO

        #Proceso

        impuesto_calculado= logica_calculadora_impuestos.calcular_impuestos(ingresos_anuales, deducciones, pension, salud, dependientes, vivienda_propia)

        #Salida

        self.assertAlmostEqual(impuesto_calculado, 629344.6, 2)

    def test_normal_2(self):
        
        #Entradas

        ingresos_anuales= 150000000
        deducciones= 20000000
        pension= 12000000
        salud= 6000000
        dependientes= 1
        vivienda_propia= 0 # 1 es SI y 2 es NO

        #Proceso

        impuesto_calculado= logica_calculadora_impuestos.calcular_impuesto(ingresos_anuales, deducciones, pension, salud, dependientes, vivienda_propia)

        #Salida

        self.assertAlmostEqual(impuesto_calculado, 12500122.6, 2)
    
if __name__ == 'main':
    unittest.main()