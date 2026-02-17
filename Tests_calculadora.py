import unittest

#Casos extraordinarios
class TestCalculadoraImpuestos(unittest.TestCase): 
    def test_extraordinario1( self ):
        #Entradas
        ingresos_anuales =6000000
        deducciones = 600000 
        pension =  48000000
        salud = 240000
        dependientes = 4 
        vivienda_propia = 1
        #Proceso
        impuesto_calculado = logica_calculadora_impuestos.calcular_impuestos(ingresos_anuales, deducciones, pension, salud, dependientes, vivienda_propia)
        #Salida 
        self.assertAlmostEqual(impuesto_calculado,20853633.5, 2)
        