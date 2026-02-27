import unittest
import logica_calculadora_impuestos
#Casos extraordinarios
class TestCalculadoraImpuestos(unittest.TestCase): 
    def test_extraordinario_1( self ):
        #Entradas
        ingresos_anuales =600_000_000
        deducciones = 60_000_000
        pension =  48_000_000
        salud = 24_000_000
        dependientes = 4 
        vivienda_propia = True # 1 es SI y 2 es NO
        interes_vivienda= 25_000_000
        #Proceso
        impuesto_calculado= logica_calculadora_impuestos.calcular_impuestos(ingresos_anuales, deducciones, pension, salud, dependientes, vivienda_propia, interes_vivienda)
        #Salida
        impuesto_esperado= 107_835_039
        self.assertAlmostEqual(impuesto_calculado, impuesto_esperado)
    
    def test_extraordianario_2(self):
        #Entradas
        ingresos_anuales = 15_000_000
        deducciones = 0 
        pension =  1_200_000
        salud = 600_000
        dependientes = 0
        vivienda_propia = False # 1 es SI y 2 es NO
        interes_vivienda= 0
        #Proceso
        impuesto_calculado= logica_calculadora_impuestos.calcular_impuestos(ingresos_anuales, deducciones, pension, salud, dependientes, vivienda_propia, interes_vivienda)
        #Salida
        impuesto_esperado= 0
        self.assertAlmostEqual(impuesto_calculado, impuesto_esperado)
        
    

if __name__ == 'main':
    unittest.main()
        