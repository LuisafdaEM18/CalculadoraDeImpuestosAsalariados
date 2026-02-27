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
        #Proceso
        impuesto_calculado = logica_calculadora_impuestos.calcular_impuestos(ingresos_anuales, deducciones, pension, salud, dependientes, vivienda_propia)
        #Salida 
        impuesto_esperado= 125_121_801
        self.assertAlmostEqual(impuesto_calculado, impuesto_esperado, 2)
    
    def test_extraordianario_2(self):
        #Entradas
        ingresos_anuales =6_000_000
        deducciones = 600_000 
        pension =  48_000_000
        salud = 240_000
        dependientes = 4 
        vivienda_propia = True # 1 es SI y 2 es NO
        #Proceso
        impuesto_calculado = logica_calculadora_impuestos.calcular_impuestos(ingresos_anuales, deducciones, pension, salud, dependientes, vivienda_propia)
        #Salida 
        impuesto_esperado= 0
        self.assertAlmostEqual(impuesto_calculado, impuesto_esperado, 2)
        


if __name__ == 'main':
    unittest.main()
        