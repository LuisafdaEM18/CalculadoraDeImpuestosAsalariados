import unittest

import sys
sys.path.append('src')

from model import logica_calculadora_impuestos


class TestCalculadoraImpuestos(unittest.TestCase): 
    def test_ingresos_negativos( self ):
        #Entradas
        ingresos_anuales = -50_000_000
        deducciones = 5_000_000
        pension = 4_000_000
        salud = 2_000_000
        dependientes = 1 
        vivienda_propia = True
        interes_vivienda= 3_000_000
        
        with self.assertRaises(logica_calculadora_impuestos.ErrorIngresos):
            impuesto_esperado= logica_calculadora_impuestos.calcular_impuestos(ingresos_anuales,deducciones,pension,salud,dependientes,vivienda_propia, interes_vivienda)

    def test_deducciones_excesivas( self ):
        #Entradas
        ingresos_anuales = 50_000_000
        deducciones = 60_000_000
        pension = 4_000_000
        salud = 2_000_000
        dependientes = 1 
        vivienda_propia = False
        interes_vivienda= 0
        
        with self.assertRaises(logica_calculadora_impuestos.ErrorTopesDeducciones):
            impuesto_esperado= logica_calculadora_impuestos.calcular_impuestos(ingresos_anuales,deducciones,pension,salud,dependientes,vivienda_propia, interes_vivienda)   
    
    def test_dependientes_negativos( self ):
        #Entradas
        ingresos_anuales = 80_000_000
        deducciones = 10_000_000
        pension = 6_400_000
        salud = 3_200_000
        dependientes = -2
        vivienda_propia = True
        interes_vivienda= 5_000_000
        
        with self.assertRaises(logica_calculadora_impuestos.ErrorDependientes):
            impuesto_esperado= logica_calculadora_impuestos.calcular_impuestos(ingresos_anuales,deducciones,pension,salud,dependientes,vivienda_propia, interes_vivienda) 

    def test_aportes_negativos( self ):
        #Entradas
        ingresos_anuales = 100_000_000
        deducciones = 15_000_000
        pension = -8_000_000
        salud = 4_000_000
        dependientes = 2
        vivienda_propia = True
        interes_vivienda= 6_000_000
        
        with self.assertRaises(logica_calculadora_impuestos.ErrorPension):
            impuesto_esperado= logica_calculadora_impuestos.calcular_impuestos(ingresos_anuales,deducciones,pension,salud,dependientes,vivienda_propia, interes_vivienda) 

    def test_interes_negativos( self ):
        #Entradas
        ingresos_anuales = 90_000_000
        deducciones = 12_000_000
        pension = 7_200_000
        salud = 3_600_000
        dependientes = 1
        vivienda_propia = True
        interes_vivienda= -3_000_000
        
        with self.assertRaises(logica_calculadora_impuestos.ErrorInteresVivienda):
            impuesto_esperado= logica_calculadora_impuestos.calcular_impuestos(ingresos_anuales,deducciones,pension,salud,dependientes,vivienda_propia, interes_vivienda) 
if __name__ == 'main':
    unittest.main()